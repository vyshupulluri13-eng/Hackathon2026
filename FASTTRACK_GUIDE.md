# Amazon fast-track guide (First Commit, Bharat Builds Tour)

Nobody can guarantee a fast-track interview. The judges, organisers and Amazon decide, and at most 10 students go forward per hackathon. This guide makes sure you don't lose points on things you control.

## 0. Timing
First Commit runs Sep 17-20, 2026 online. Today (Sep 20) is the last day. Open the hackathon page now and check the exact submission deadline.

## 1. Eligibility (check before anything else)
- [ ] University student in India, pre-final year (2028 batch) or final year (2027 batch)
- [ ] Registered for the tour and checked in to First Commit
- [ ] AWS Builder Center profile with enrollment verified (SheerID)
- [ ] Registration details match your Builder Center profile
- [ ] Each teammate qualifies and registered with their own account

Winning a prize is neither required nor enough. Projects are judged separately for the interview.

## 2. Judging criteria and what to do

| Criterion | What to do |
|---|---|
| Idea and Impact | Pick ONE real problem and name who has it. A small problem solved well beats a big vague one. |
| Built on AWS | Ship It track: deploy live on AWS and submit a URL. The architecture is scored. |
| Learning | Write what you learned in these days (a first deploy, a first Bedrock call, and so on). |
| Execution | It must work. One feature that runs beats five that almost do. |
| Demo video | 3 minutes: what it does, who it's for, where AWS fits. There is no live demo. |

## 3. Sharpen the idea
"Summarise notes and make a quiz" is generic, and many teams will build it. Make it about a specific person and problem, for example:

- Students who read English notes but think best in Hindi or another Indian language (the API already accepts a `language` field).
- Show real before/after: ask 3 to 5 classmates to try it and note what they said.

Replace the placeholder below with YOUR real story. Judges want something that matters to you.

> **Problem:** _who struggles with what, and how you know_
> **Solution:** _what StudyBuddy changes for them_

## 4. Ship It architecture notes (scored)
- Fully serverless, so you pay only per request and stay inside Free Tier and credits.
- Input is capped at 20,000 characters to control Bedrock cost.
- Set an AWS Budget alert before you start.
- Optional extras if time allows: Cognito for login, CloudWatch for logs.

## 5. Demo video script (3 minutes)
1. **0:00-0:30** The problem and who has it
2. **0:30-1:30** Live walkthrough: paste notes, pick language, get summary and quiz
3. **1:30-2:30** AWS console: show Lambda, Bedrock, API Gateway, DynamoDB and the architecture
4. **2:30-3:00** What you learned and what's next

## 6. Submission checklist
- [ ] Live URL works in a private browser window
- [ ] Demo video recorded and uploaded (3 min max)
- [ ] Writeup complete (see the template in README.md), with AI tools listed
- [ ] Third-party code and libraries credited
- [ ] Optional: blog post on AWS Builder Center, linked in the submission (top 5 blogs win a keyboard)
- [ ] Submitted before the deadline
