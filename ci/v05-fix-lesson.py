from pathlib import Path

path = Path('source/android/feature/lesson/src/main/java/com/masterlearner/feature/lesson/LessonScreen.kt')
text = path.read_text()
old = '                        if (s.problem.secondaryAction != null) MasterSecondaryButton(s.problem.secondaryAction, onBack, Modifier.weight(1f))'
new = '                        s.problem.secondaryAction?.let { secondaryAction ->\n                            MasterSecondaryButton(secondaryAction, onBack, Modifier.weight(1f))\n                        }'
if old not in text:
    raise SystemExit('Expected nullable secondaryAction expression missing')
path.write_text(text.replace(old, new, 1))
print('Bound nullable secondaryAction before cross-module Compose call')
