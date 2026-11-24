# PRD: App Stability & Release Quality (Telegram for Android)

| | |
|---|---|
| **Author** | Chariyan Dharmesh Ekka (portfolio case study) |
| **Status** | Draft for review |
| **Priority** | #1 on the review-driven backlog (RICE 59) |
| **Evidence** | 22,816 Google Play reviews, Nov 2016 – May 2017 ([analysis notebook](../notebooks/01_review_insights.ipynb)) |

## 1. Problem
Users who mention crashes, bugs or the app "not working" rate Telegram **2.90★, against 4.39★ overall**, and 44% of them leave 1–2★. The theme appears in **7.2% of all 1–2★ reviews** (incident excluded), and unsupervised topic modelling surfaces a separate "new update broke it, please fix" topic.

Among the 187 dissatisfied (≤3★) reviews about crashes and bugs:

| Where it breaks | Share of those reviews |
|---|---|
| Sending / loading messages | 20% |
| Photos, videos and other media | 18% |
| Opening or starting the app | 17% |
| Notifications (e.g. an unread badge that won't clear) | 14% |
| Right after an update | 13% |

*Example voices:* "Crashes immediately upon opening it." · "The latest update is full of bugs… It's literally causing my device hang and force-restart." · "Unread notification at icon won't go away."

## 2. Goals and success metrics

| Type | Metric | Target |
|---|---|---|
| **Primary** | Crash-free sessions (Android) | ≥ 99.5% (baseline to be measured in week 1) |
| Primary | Share of 1–2★ reviews mentioning crashes/bugs | −50% within two releases |
| Secondary | App-start crash rate | < 0.1% of launches |
| Secondary | Average rating of reviews mentioning updates | +0.5★ |
| **Guardrail** | Release cadence | No slower than today's |
| Guardrail | App size and cold-start time | No regression > 5% |

*Targets are proposals to agree with engineering after the baseline is measured.*

## 3. Users and use cases
- **As a user on a low-end Android phone**, I want the app to open reliably after an update, so I don't miss messages.
- **As a user sending photos and videos**, I want sending to finish or fail clearly, so I know whether my message went.
- **As a user who hit a bug**, I want to report it in two taps with logs attached, so it actually gets fixed.

## 4. Requirements

| # | Requirement | Priority |
|---|---|---|
| R1 | Crash and ANR (app-not-responding) reporting grouped by device, OS version and app version, with a daily release-health dashboard | Must |
| R2 | **Staged rollout gate:** each release goes 1% → 10% → 50% → 100%, and only advances if crash-free sessions ≥ 99.5% and there is no new top-10 crash cluster | Must |
| R3 | Fix the top 10 crash clusters by affected users, starting with app-start crashes | Must |
| R4 | Clear failed-send state for messages and media (retry button, no silent failure) | Should |
| R5 | In-app "Report a problem" (shake or Settings → Help) that attaches logs and device info, with consent | Should |
| R6 | Recompute the unread-badge count on app open to fix the stuck-badge bug | Should |
| R7 | Weekly review-mining job that tracks the crash/bug theme share as a user-facing health metric | Could |

**Out of scope:** new features, redesigns, and iOS (separate review).

## 5. Rollout and measurement plan
1. **Week 1:** ship R1 and measure the baseline crash-free rate and top clusters.
2. **Weeks 2–6:** fix clusters (R3) behind the staged rollout gate (R2).
3. **Measure:** compare crash-free sessions release over release, and the theme share in reviews for 4 weeks before vs after. Treat review share as directional only, since reviews are a self-selected sample.

## 6. Risks and open questions
- Device fragmentation: some crashes may be OEM-specific and hard to reproduce. Mitigation: test on the top 20 devices by crash volume.
- Staged rollouts slow releases a little. Mitigation: auto-advance when the gates pass.
- **Open:** do we have consent-compliant logging in every region? This needs a legal review before R5.

## 7. Why this first (RICE summary)

| Initiative | Reach / qtr | Impact | Confidence | Effort (PM) | RICE |
|---|---|---|---|---|---|
| **Crash & stability programme** | 99 | 3 | 80% | 4 | **59** |
| Faster media downloads on slow networks | 266 | 1 | 80% | 4 | 53 |
| Reliable notifications | 94 | 2 | 80% | 3 | 50 |

Reach = dissatisfied (≤3★) reviews per quarter mentioning the theme. Effort is the PM's estimate and should be validated with engineering.
