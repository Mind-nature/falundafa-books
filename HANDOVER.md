# 交接文件 — 法輪大法閱讀版

> 開新對話（雲端版或本地版 Claude）時，說「讀 HANDOVER.md 繼續」即可同步全部狀態。
> 每次進度有變，請 Claude 更新這份檔案。
> 最後更新：2026-08-01

---

## 專案基本資訊

| 項目 | 內容 |
|---|---|
| 網站 | https://mind-nature.github.io/falundafa-books/ |
| repo | Mind-nature/falundafa-books（部署分支 main） |
| 首頁 repo | Mind-nature/mind-nature.github.io（放 .well-known/assetlinks.json） |
| App 形式 | TWA（用 PWABuilder 打包） |
| App 名稱 | 法輪大法閱讀版（桌面短名：法輪書籍） |
| Package ID | io.github.mind_nature.falundafabooks |
| 帳號類型 | 個人開發者帳號（適用 12 人×14 天封閉測試規定） |
| ★ 正式版商店連結 | https://play.google.com/store/apps/details?id=io.github.mind_nature.falundafabooks |

### 本機檔案位置（不在 git，僅本地/雲端硬碟）
- 上架素材：`D:\WORKCL\falundafa_books_release\`
  - `1_keys/` — 簽署金鑰 signing.keystore（密碼記於該資料夾，另有加密備份在 Google Drive）
  - `2_app/` — 目前版本 .aab/.apk + 歷史版本/
  - `3_store_listing/` — 圖示、特色圖、7 張截圖、文案
  - `9_archive/` — 最新完整包 zip + assetlinks 備份
  - `README.txt` — 打包/上傳 SOP（含金鑰密碼）
  - `封閉測試操作手冊.txt` — 招募、群組訊息範本、每日盯場清單

---

## Google Play 上架進度

### 現況（2026-07-30）：🎉 正式版已上架！
- 7/30 收到 email：正式版權限申請通過（7/23 送出，審查 7 天）
- 7/30 建立正式版版本（v1.0.4 / code 5，從檔案庫帶入，不用重新上傳 AAB）
- 國家/地區：**只開放台灣**（低調路線；之後要擴充隨時可加，即時生效、免審查）
- 已通過審查並全面推出，一般用戶在台灣 Play 商店可直接搜尋安裝
- 測試員帳號看到的名稱會帶「(Beta 版)」標籤，一般用戶看到的是乾淨名稱（正常現象）
- 分級：IARC 3+ 已生效（收到 Live Rating Notice 通知信，制式信件、免處理）

### ★ 被退 3 次後、客服證實的真正敗因
> 「每日活躍測試者 ≥ 12 人，連續 14 天，**每一天**都要達標」
> （不是平均、不是每月活躍）

前 3 次都輸在「某幾天每日活躍掉到 5~8 人」。
上一輪：每月活躍 47、總安裝 42，但每日活躍平均只有 9.71、最高 14。

**這次唯一要贏的關鍵：7/9 起連續 14 天，每一天都要 ≥ 12 人打開 App。**

### 第四輪時程（7/9 起算）
| 日期 | 天數 | 動作 |
|---|---|---|
| 7/9 | Day0 | ✅ 上傳 v1.0.3、發開跑訊息 |
| 7/10–7/22 | 1–13 | ✅ 每天發提醒，每日活躍守住 12+ |
| 7/15 | Day6 | ✅ 推 v1.0.4（書籤計數）並上傳 Play |
| 7/23 | Day14 | ✅ 三條件達標，送出正式版權限申請（上午 3:37） |
| 7/23–30 | — | ✅ 等待審查（7 天） |
| 7/30 | — | ✅ 收到通過通知 → 設定台灣 → 建立正式版（code 5）→ 審查通過、全面推出 🎉 |

---

## 版本紀錄

| 版本 | code | 日期 | 內容 |
|---|---|---|---|
| 1.0.0 | 1 | 5/22 | 首版 |
| 1.0.1 | 2 | 6/27 | 載入動畫呼吸脈動、toast 淡出 |
| 1.0.2 | 3 | 7/5 | 搜尋群組標題配色、關鍵字高亮 |
| 1.0.3 | 4 | 7/9 | 回到頂部浮動按鈕、搜尋樣式微調 |
| 1.0.4 | 5 | 7/15 | 書籤面板標題顯示數量計數（X / 10） |
| 1.0.5 | 6 | 8/1 | targetSdk 升級 36（Bubblewrap CLI 本機打包），待上傳 |

---

## 待辦事項（上架後）

- [x] **targetSdk 升級 36** ✅ 8/1 已用本機 Bubblewrap CLI 1.25.0 打包完成
  - v1.0.5 / code 6，已驗證：targetSdk 36、versionName 1.0.5、簽章與上傳金鑰一致
  - 檔案在 `2_app/法輪大法閱讀版.aab`，**待上傳 Play Console 正式版軌道**
  - 本機打包環境已建好（之後可重複用，不再依賴 PWABuilder 網站）：
    - 專案：`falundafa_books_release/4_bubblewrap/`（twa-manifest.json 為設定檔）
    - 工具：`C:\Users\adminininin\.bubblewrap\`（JDK 17 + Android SDK）
    - 下次更新流程：改 twa-manifest.json 的 appVersion/appVersionCode →
      `bubblewrap update --skipVersionUpgrade` → 手動 gradlew bundleRelease → jarsigner 簽署
      （細節見 README.txt 的 Bubblewrap 流程）
- [ ] 上傳 v1.0.5 至正式版並送審（順便觀察 Play Console 四項建議是否消失）
- [ ] 可考慮之後做「完整離線閱讀」（把全部書籍 HTML 加進 sw.js 的 PRECACHE）
- [ ] 發感謝訊息給測試群組，告知正式版已上架，分享正式版連結
- [ ] 請夥伴到商店頁留「公開評論」（正式版才有；測試期的私人意見不算）→ 有助搜尋排名
- [ ] 測試員去留：可自由退出（退出後變一般用戶、照常收更新）；建議留幾位在測試軌道，日後新版先試再推正式
- [ ] 推廣以直接分享正式版連結為主（新 App 搜泛關鍵字排名低是正常，靠評論與安裝數慢慢爬）
- [ ] 之後想擴地區：Console → 正式版 → 國家/地區 勾選即可，即時生效免審查

---

## 常用操作

### PULL（同步網站 repo 最新）
本地版：`git pull`（在 D:\WORKCL\falundafa_books）

### 更新 App 流程（推新版）
1. PWABuilder（https://www.pwabuilder.com）輸入網站網址 → Android → Google Play
2. Package ID：io.github.mind_nature.falundafabooks（務必一致）
3. Version code 每次 +1（目前最新 5，下次填 6）
4. Signing key 選 Use mine，上傳 1_keys/signing.keystore
5. 下載 → 解壓找 .aab → Play Console 封閉測試建立新版本上傳送審
6. 詳細步驟見本機 README.txt

### 重要觀念
- 網站內容（HTML/CSS/JS）改了 push GitHub 就即時生效，App 自動抓最新，不用重打包。
- 重新打包 AAB 主要是為了封閉測試期間的「版本更新活動」。
- assetlinks.json 已掛好兩個指紋（上傳金鑰 + Google 簽署金鑰），除非換金鑰否則不用動。

---

## 群組訊息範本（複製即用）

### 三個自助連結
- 群組：https://groups.google.com/g/mind-nature_test
- 測試：https://play.google.com/apps/testing/io.github.mind_nature.falundafabooks
- 下載：https://play.google.com/store/apps/details?id=io.github.mind_nature.falundafabooks

### 【開跑訊息】第四輪重啟，發一次
```
🙏 各位夥伴，App 測試重新開始囉！

已經裝好的朋友不用重裝，Google Play 有更新的話點一下更新即可 🙏

━━━━━━━━━━━━━━━━━━━━━━━━
🔴 這次最重要的一件事（拜託大家）：

接下來 14 天，請「每天」打開這個 App
一天只要 1-2 分鐘（滑一滑、看一段就好）
中途請「不要移除」App

Google 規定要「每一天」都有足夠的人打開，
只要某一天人數不夠，測試就要重來 😭
（前幾次就是卡在這，這次真的拜託大家幫忙）
━━━━━━━━━━━━━━━━━━━━━━━━

還沒安裝的朋友，三步驟：
1️⃣ 加入群組：https://groups.google.com/g/mind-nature_test
2️⃣ 成為測試員：https://play.google.com/apps/testing/io.github.mind_nature.falundafabooks
3️⃣ 下載：https://play.google.com/store/apps/details?id=io.github.mind_nature.falundafabooks
（步驟 1、2 要用同一個 Google 帳號）

真的很感謝大家，這次一起讓它上架 🙏
```

### 【每日提醒】每天早上發一則（維持每日活躍 ≥ 12）
最簡版：
```
📱 早安～今天也記得打開 App 滑一下喔（1 分鐘就好）謝謝大家 🙏
```
帶天數版：
```
🙏 早安～測試第 X 天
今天也麻煩打開 App 1 分鐘，謝謝大家幫忙 🙏
```

### 【活躍不足加強版】當天活躍 < 12 人時發
```
⚠️ 今天還差幾位打開 App，拜託還沒開的朋友幫忙開一下～
只要 1 分鐘，不然測試會前功盡棄 🙏🙏
```

### 【版本更新提醒】推新版時發（第 6、12 天）
```
📲 App 出新版本囉，麻煩到 Google Play 更新一下
（Play 商店 →「法輪大法閱讀版」→ 點「更新」）

⭐ 有空的話，歡迎從 Play 商店測試頁面送「意見回饋」
（Google 看得到這個管道，對審核通過有幫助 🙏）

⚠️ 也提醒大家「每天」打開 App，中途不要移除 🙏
```
