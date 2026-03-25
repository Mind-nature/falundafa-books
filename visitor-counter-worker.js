// Cloudflare Worker - 瀏覽人次計數器 (IP 去重)
//
// 部署步驟：
// 1. 登入 Cloudflare Dashboard → Workers & Pages → Create Worker
// 2. 貼上此程式碼
// 3. 建立 KV Namespace：Workers & Pages → KV → Create Namespace，取名 "VISITOR_DATA"
// 4. 綁定 KV：Worker Settings → Variables → KV Namespace Bindings
//    - Variable name: VISITOR_DATA
//    - KV Namespace: 選擇剛建立的 "VISITOR_DATA"
// 5. 部署後將 Worker URL 填入 index.html 中的 VISITOR_COUNTER_API 變數
//
// KV 儲存結構：
//   key: "ip:<hashed_ip>"  → value: "1"  (記錄已訪問的 IP)
//   key: "total_count"     → value: "123" (總瀏覽人次)

export default {
  async fetch(request, env) {
    // CORS 設定
    const corsHeaders = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    };

    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders });
    }

    if (request.method !== 'GET') {
      return new Response('Method not allowed', { status: 405, headers: corsHeaders });
    }

    try {
      // 取得訪客 IP
      const ip = request.headers.get('CF-Connecting-IP') || 'unknown';

      // 用 SHA-256 雜湊 IP（隱私保護，不存原始 IP）
      const ipHash = await hashIP(ip);
      const ipKey = `ip:${ipHash}`;

      // 檢查此 IP 是否已計算過
      const existing = await env.VISITOR_DATA.get(ipKey);

      let totalCount = parseInt(await env.VISITOR_DATA.get('total_count') || '0', 10);

      if (!existing) {
        // 新 IP，計數 +1
        totalCount += 1;
        await env.VISITOR_DATA.put(ipKey, '1');
        await env.VISITOR_DATA.put('total_count', totalCount.toString());
      }

      return new Response(JSON.stringify({ count: totalCount }), {
        headers: {
          'Content-Type': 'application/json',
          ...corsHeaders,
        },
      });
    } catch (err) {
      return new Response(JSON.stringify({ error: 'Internal error' }), {
        status: 500,
        headers: { 'Content-Type': 'application/json', ...corsHeaders },
      });
    }
  },
};

async function hashIP(ip) {
  const encoder = new TextEncoder();
  const data = encoder.encode(ip);
  const hashBuffer = await crypto.subtle.digest('SHA-256', data);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
}
