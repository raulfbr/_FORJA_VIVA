# 🚀 PILOT SPRINT WORKFLOW
> *Workflow for the first production sprint.*

---
name: pilot-sprint
version: "1.0"
description: "First sprint to validate the Forja system"
estimated_duration: 5 days
---

## 1. Objective

Execute the first complete sprint to validate:
- Agent flow (Orchestrator → PM → SM → Dev → QA → Ops)
- Templates and checklists
- Quality standards

---

## 2. Sprint Scope

| Item | Target |
|------|--------|
| Stories | STORY-001 to STORY-005 |
| Epic | EPIC-001 (Foundation) |
| Output | 5 approved lessons |

---

## 3. Phase 1: PLANNING (Day 1)

### 3.1 Orchestrator
- [ ] Define sprint goal
- [ ] Assign agents to stories
- [ ] Set deadline

### 3.2 PM
- [ ] Review Epic requirements
- [ ] Validate story priorities
- [ ] Approve PRD

---

## 4. Phase 2: DEVELOPMENT (Days 2-4)

### 4.1 SM (Per Story)
- [ ] Create Story File with full context
- [ ] Validate CPA checklist present
- [ ] Assign to Dev

### 4.2 Dev (Per Story)
- [ ] Write complete lesson
- [ ] Self-check against criteria
- [ ] Mark as ready for QA

### 4.3 QA (Per Story)
- [ ] Execute 5-Pass Verification
- [ ] Mark as APPROVED/REJECTED
- [ ] If rejected, return to Dev with notes

---

## 5. Phase 3: RELEASE (Day 5)

### 5.1 Ops
- [ ] Migrate approved lessons to `curriculo/`
- [ ] Archive draft versions
- [ ] Update status log

### 5.2 Orchestrator
- [ ] Generate sprint report
- [ ] Present to Maestro for final approval

---

## 6. Definition of Done

| Criterion | Status |
|-----------|--------|
| 5 lessons approved by QA | ✅/❌ |
| All migrated to production | ✅/❌ |
| Maestro final approval | ✅/❌ |
| Sprint report generated | ✅/❌ |

---

## 7. Sprint Report Template

```markdown
# 📊 SPRINT REPORT

**Sprint:** Pilot Sprint
**Date:** [Date]
**Status:** ✅ COMPLETE / ❌ INCOMPLETE

## Summary
| Metric | Target | Actual |
|--------|--------|--------|
| Stories | 5 | [X] |
| Approved | 5 | [X] |
| Rejected | 0 | [X] |

## Lessons Produced
1. STORY-001: [Title] — ✅/❌
2. STORY-002: [Title] — ✅/❌
3. STORY-003: [Title] — ✅/❌
4. STORY-004: [Title] — ✅/❌
5. STORY-005: [Title] — ✅/❌

## Issues Encountered
- [Issue 1]
- [Issue 2]

## Recommendations for Next Sprint
- [Recommendation 1]
- [Recommendation 2]

## Signature
> Orchestrator, [Date]
```

---

> *"The pilot sprint validates the system. If it works here, it works everywhere."*
