# Continuous-Action Director Cards

Use this module when a multi-panel image will be uploaded directly to Seedance as the shot-and-motion reference, especially for combat, chase, rescue, transformation, or any 10-15 second clip with tightly connected actions.

## Standalone Clip Versus Cross-Clip Continuation

- A director card describes one self-contained video clip by default. Its first row must show a visible starting pose and a first action that does not depend on another segment number.
- Use previous/next clip boundary fields only when the user explicitly asks for video extension, action-match continuation, or a stitched sequence. Otherwise mark the card `standalone clip` and use no unexplained previous-clip references.
- “Previous clip” is a production note, not an instruction Seedance can infer. Never put “承接S08/S09” or an equivalent unexplained segment reference into a standalone handoff prompt.

## Director Card Versus Review Storyboard

- An ordinary storyboard proves composition, story order, and coverage.
- A director card tells the video model how one clip moves through time.
- Do not upload a review board as the primary motion reference when its panels are independent static target poses.
- Keep the ordinary board for story review; create a versioned director card when motion continuity matters.

## Inputs To Lock Before Designing The Card

Read the current script, previous and next clip endings, character and monster references, clean scene resources, prop count, effect references, and the current Seedance prompt.

Write a boundary contract:

```text
Previous clip exits while:
This clip begins by:
This clip must not repeat:
This clip exits while:
Next clip begins by:
```

The first shot must continue the previous clip's force, body orientation, weapon position, and screen direction. Do not replay the previous clip's completed attack. End with an unfinished recover, turn, fall, reach, or camera occlusion so the next clip can use an action-match cut.

## Build One Causal Action Chain

Use three to four timed beats for most 15-second action clips:

1. **Immediate continuation** — resolve the incoming force or finish the already-started move.
2. **Counter and response** — attacker and defender act in the same shot.
3. **Escalation and consequence** — the second threat exploits the recovery; show contact and body result.
4. **Moving exit** — recover, roll, turn, rise, or occlude while motion is still continuing.

Every beat needs:

- visible full-body mechanics or the minimum framing required to read them;
- opponent reaction in the same spatial axis;
- camera path and lens/framing intent;
- action trigger, contact point, force direction, and physical consequence;
- explicit weapon count and blade position;
- a start state that inherits the prior beat and an exit state that creates the next beat.

Effects stay in the same shot as the action that creates them. If smoke reforms while a tail counterattacks, show both events together. Do not isolate the effect as a beauty shot or pause the actor to watch it.

## Default Quantitative Guardrails

Use these as starting caps for a 15-second combat clip, then adjust only when the story requires it:

| Risk | Starting guardrail |
|---|---|
| Static montage behavior | Three to four beats, not five or six equal-duration poses |
| Lost fight readability | Full-body interaction occupies at least 70% of the clip |
| Monster or effect showcase | Any isolated insert stays at or below 0.5 seconds |
| Completed-pose freeze | No completed pose holds longer than 0.5 seconds |
| Weapon/contact fixation | Contact normally clears within 0.4 seconds |
| Transitional drag or slide | A sword-tip drag or similar stabilizing action stays below 1.2 seconds |

These are prompt guardrails, not editing-frame laws. Tighten them after a failed render; do not add arbitrary numbers that have no visible failure to prevent.

## Spatial And Resource Isolation

- Use a clean scene or empty scene image to lock terrain and camera direction.
- Bind character, monster, prop, and effect references separately.
- Avoid a scene resource that already contains people, monsters, or the decisive effect; the model may copy that embedded composition instead of following the director card.
- If a composite reference is unavoidable, label it `spatial reference only` and state that its pose, action, and character placement must not be copied.
- State left/right, foreground/midground/background, who faces whom, camera side, screen direction, and the forbidden reverse position.
- Use one weapon or single weapon when the story calls for one; keep it outside the torso silhouette whenever overlap could read as self-impalement.

## Card Layout

Prefer one portrait card per clip:

1. Title: segment, duration, version, and continuity purpose.
2. Overview staging diagram: camera, axis, screen direction, all actors, and force arrows.
3. Three or four timed shot rows. Each row pairs one readable image with action, camera, sound, and constraint text.
4. Hard constraints footer: continuity, interaction share, hold limits, weapon count, and exit state.

For combat, chase, rescue, or crowd-control clips, the overview staging diagram is mandatory and should be a simple top-down / overhead / bird's-eye map, not a cinematic beauty frame. It must show the axis, camera position, screen direction, actor positions, attack lanes, force arrows, and forbidden reverse placement. Label it as `Overview only, not shot 1`; the first video shot starts in the first timed shot row.

The image must communicate the action without relying on the text. Labels and arrows clarify; they cannot rescue an ambiguous pose.

## Image QA Before Publishing

Inspect the actual bitmap at original resolution:

- Every row differs in action and camera purpose.
- For combat, chase, rescue, or crowd-control clips, the top block is a top-down overview map and does not read as the first video shot.
- Character faces the opponent, not the viewer, unless the shot explicitly requires it.
- Water, smoke, or terrain height matches the written contact point.
- The weapon is complete, singular, outside the chest/abdomen, and aimed at the intended target.
- A strike that only cuts aura leaves a clear gap between the split aura and the intact body.
- Opponents remain on their assigned screen sides.
- The final row shows active recovery or transition, not a seated or completed hero pose.
- Text is readable enough to identify each row, but Seedance instructions remain in the Markdown prompt as the canonical wording.

If one row is wrong, edit only that row and preserve the approved rows, overview, title, and text.

## Seedance Handoff

Upload the director card as the primary motion reference. Upload clean scene, identity, prop, monster, and effect images only as appearance locks. In the prompt, map each timed block to the matching card row and tell the model that card labels, arrows, borders, and text must not appear in the video.

Use action-match cut or cut during motion at the end. Do not ask the model to reach a finished poster pose and then hold it.

## Feedback And Versioning

After reviewing a downloaded video:

1. Record the actual behavior by time range, not by impression.
2. Identify whether the first wrong instruction lives in the script, card, resource binding, or Seedance prompt.
3. Revise the earliest source and propagate downstream.
4. Save a new card version; do not overwrite the approved or tested file.
5. Archive the stale card with a short failure reason in its filename.
6. Keep only the current version in the production directory and update every active reference.
7. Run regression checks for both the revised clip and its neighboring clip boundaries.

## Compact Example

For a hero fighting two monsters:

```text
0-3.5s: continue the prior recovery and complete one upward counter-slash; cut only the outer aura.
3.5-7s: aura reforms while the same monster launches a tail counter; hero lowers the weapon into recovery.
7-10.5s: hero redirects the tail down-right with one weapon; the second monster's wave hits legs and hip after the redirect.
10.5-15s: sword tip drags for about one second, then lifts; hero rolls and begins to recover; cut during motion.
```

This is one fight chain, not four independent demonstrations.

## Common Mistakes

- Repeating the previous clip's final move as the new opening.
- Giving every panel equal duration and asking Seedance to visit each pose.
- Showing smoke, magic, a foot, or a weapon alone while the fight pauses.
- Letting the image contradict the text on water height, weapon direction, or facing.
- Keeping a composite resource with actors inside the scene-reference slot.
- Updating the card but leaving the Seedance index, checklist, or manifest bound to the older version.
