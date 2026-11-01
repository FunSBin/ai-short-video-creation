# Validation And Feedback

Use this module after drafts, generated images, black-and-white boards, or Seedance tests.

## Cross-Document Validation

Check all active documents together:

- Script event order.
- Resource list and generated files.
- Storyboard script shot order.
- Black-and-white board panel order.
- Seedance prompt clip order.
- User test feedback.

## Continuity Checklist

- Is the scene before or after the key action?
- Has a prop left a hand, broken, transformed, or flown away?
- Did a new object appear without being referenced?
- Did an effect appear before the action that causes it?
- Does the next clip contradict the previous clip?

## Staging Checklist

- Who is in foreground, midground, background?
- Who faces camera?
- Who faces another character?
- Who is back or side-back to camera?
- Where is the camera standing?
- What is the correct background for this camera direction?
- What background must not appear?
- Does each used area/direction have actual scene coverage, including both backgrounds of planned shot/reverse-shot? Use [scene coverage](../../ai-short-video-assets/references/scene-coverage.md) to check paired views and shot-to-image mapping.
- Across same-scene representative frames, did planned direction changes produce corresponding perspective, occlusion and landmarks? Repeated local compositions need a narrative reason; text-only review is not visual verification.

## Asset Binding Checklist

- Every named character has a `CHAR_` or bound role reference.
- Every named scene has a `SCENE_` reference.
- Every prop has a `PROP_` reference.
- Every monster or divine form has the correct reference.
- Before and after state scenes are not swapped.

## Lip-Sync Checklist

- Visible dialogue has a named lip-sync owner.
- Off-screen dialogue is explicitly marked as off-screen or voice-over.
- Other visible characters are told not to speak.
- Long lines are given enough seconds or split into clips.
- The line remains coherent after any shortening.

## Feedback Backfill

When the user reports a failure:

1. Identify whether the failure belongs to script, resource, board, or video prompt.
2. Fix the earliest causal document or earliest source document that caused the issue.
3. Propagate the correction downstream.
4. Keep only one canonical current version when possible; archive older versions.
5. Re-run structure checks after editing.

## Downloaded Video Review

When the user provides a downloaded video, inspect the file rather than judging from the prompt:

1. Confirm duration, resolution, frame rate, and whether the final seconds contain a frozen or repeated pose.
2. Sample the full clip at regular intervals, then inspect suspicious action boundaries more densely.
3. Record observations by time range: who is visible, body orientation, weapon position, contact, camera behavior, effect timing, and motion continuity.
4. Compare the rendered sequence with the director card, Seedance time blocks, previous clip exit, and next clip entry.
5. Classify the first failure as script logic, ambiguous card image, contaminated resource, conflicting references, prompt timing, or model variance.

Do not call a fight weak only because it “feels static.” State the visible symptom, such as independent monster showcases, repeated contact pose, missing counterattack, or a completed pose held for several seconds.

## Canonical Version And Regression

- Save a revised card with a new version; never overwrite the tested source.
- Archive stale cards with a concise failure reason in the filename.
- Keep only the current version in the production directory.
- Update the Seedance index, prompt body, continuity checklist, and asset manifest together.
- Regression-check the revised clip, the prior clip's exit, the next clip's entry, active file references, image dimensions, weapon count, and forbidden old bindings.
- A text check does not replace visual QA of the bitmap or downloaded video.

## Common Corrections

- Wrong staging: add camera-side, facing, foreground, background, and negative background constraints.
- Repetitive local background: first check missing area/view assets, then storyboard mapping and actual bindings. Supplement the earliest missing view; do not rely on more camera adjectives or upload the entire scene pack. Retain approved shots.
- Wrong prop state: bind the prop and clarify whether it is in hand, flying away, broken, or absent.
- Wrong effect timing: add before-state and after-state scene references.
- Mouth not moving: add lip-sync owner and shorten or lengthen the line logically.
- Prompt and board mismatch: either update the board, update the prompt, or explicitly mark the board panel as only a spatial diagram.
- Static montage: reduce independent target poses, combine effect and counterattack in the same shot, and end with cut during motion.
- Wrong reference influence: replace populated scene references with clean empty scenes and bind identities separately.
