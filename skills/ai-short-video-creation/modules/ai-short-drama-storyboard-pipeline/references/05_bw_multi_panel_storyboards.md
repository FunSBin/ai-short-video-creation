# Black-And-White Multi-Panel Storyboards

Use this module when making black-and-white line-art storyboard boards for director review.

## Ordinary Storyboard Versus Director Card

An ordinary review storyboard checks story order, framing, staging, and coverage. A direct-input director card controls one clip's timed motion. They may share black-and-white artwork, but they are not interchangeable.

Use `08_continuous_action_director_cards.md` when Seedance will receive the board as the primary action reference. Do not give a continuous fight five or six equal panels that read as independent poses or static target poses.

## Purpose

Black-and-white multi-panel storyboard boards are not final visual art. They are director checking tools for:

- staging
- camera angle
- foreground, midground, background
- who faces camera
- who is back or side-back to camera
- action direction
- prop placement
- before and after event state

## Board Rules

- Use 1x2, 1x3, 2x2, 2x3, or 3x3 layouts.
- Do not exceed 3x3.
- Choose panel count by action clarity, not by habit.
- For one continuous action clip, prefer three or four causally linked beats over a montage of equal-duration poses.
- Include clear Chinese labels and arrows in the storyboard board only when useful for review.
- In later video prompts, tell the video model not to generate the labels, arrows, or panel numbers.

## Prompt Requirements

Each multi-panel prompt must include:

```text
board filename
episode and segment
panel layout
panel-by-panel description
asset references
camera position
person facing or back-facing
foreground, midground, background
must-not-change constraints
```

## Common Failure Prevention

- If a character should face another character, do not place the other character as background behind them.
- If a river is created by a sword strike, panels before the strike must show continuous dry ground.
- If a sword action is downward, explicitly say one sword only, blade tip down, no skyward second blade.
- If a palace reverse shot faces a kneeling character, the background should be the palace door or column corridor, not the high platform again.
- If a close-up has a prop, keep nearby characters consistent with the previous panel.

## QA Checklist

- Panel count matches the prompt.
- All labels identify the correct assets.
- Staging is readable without prose.
- The important action direction is unambiguous.
- No contradictory before or after state appears too early.
- The board can be cropped into smaller references for 15-second video clips.
- If the board will be uploaded directly for motion, each panel inherits the prior panel's body orientation, force, weapon position, and screen direction.
