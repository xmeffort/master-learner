from pathlib import Path

path = Path('source/android/core/designsystem/src/main/java/com/masterlearner/core/designsystem/MasterLearnerTheme.kt')
text = path.read_text()
replacements = {
    'TextStyle(FontWeight.SemiBold, 42.sp, 46.sp, letterSpacing = (-0.9).sp)': 'TextStyle(fontWeight = FontWeight.SemiBold, fontSize = 42.sp, lineHeight = 46.sp, letterSpacing = (-0.9).sp)',
    'TextStyle(FontWeight.SemiBold, 34.sp, 39.sp, letterSpacing = (-0.65).sp)': 'TextStyle(fontWeight = FontWeight.SemiBold, fontSize = 34.sp, lineHeight = 39.sp, letterSpacing = (-0.65).sp)',
    'TextStyle(FontWeight.SemiBold, 28.sp, 34.sp, letterSpacing = (-0.4).sp)': 'TextStyle(fontWeight = FontWeight.SemiBold, fontSize = 28.sp, lineHeight = 34.sp, letterSpacing = (-0.4).sp)',
    'TextStyle(FontWeight.SemiBold, 23.sp, 29.sp, letterSpacing = (-0.18).sp)': 'TextStyle(fontWeight = FontWeight.SemiBold, fontSize = 23.sp, lineHeight = 29.sp, letterSpacing = (-0.18).sp)',
    'TextStyle(FontWeight.SemiBold, 20.sp, 26.sp, letterSpacing = (-0.1).sp)': 'TextStyle(fontWeight = FontWeight.SemiBold, fontSize = 20.sp, lineHeight = 26.sp, letterSpacing = (-0.1).sp)',
    'TextStyle(FontWeight.SemiBold, 17.sp, 23.sp)': 'TextStyle(fontWeight = FontWeight.SemiBold, fontSize = 17.sp, lineHeight = 23.sp)',
    'TextStyle(FontWeight.Medium, 15.sp, 20.sp)': 'TextStyle(fontWeight = FontWeight.Medium, fontSize = 15.sp, lineHeight = 20.sp)',
    'TextStyle(FontWeight.Normal, 17.sp, 26.sp)': 'TextStyle(fontWeight = FontWeight.Normal, fontSize = 17.sp, lineHeight = 26.sp)',
    'TextStyle(FontWeight.Normal, 15.sp, 23.sp)': 'TextStyle(fontWeight = FontWeight.Normal, fontSize = 15.sp, lineHeight = 23.sp)',
    'TextStyle(FontWeight.Normal, 13.sp, 19.sp)': 'TextStyle(fontWeight = FontWeight.Normal, fontSize = 13.sp, lineHeight = 19.sp)',
    'TextStyle(FontWeight.SemiBold, 14.sp, 18.sp, letterSpacing = 0.05.sp)': 'TextStyle(fontWeight = FontWeight.SemiBold, fontSize = 14.sp, lineHeight = 18.sp, letterSpacing = 0.05.sp)',
    'TextStyle(FontWeight.Medium, 12.sp, 16.sp, letterSpacing = 0.12.sp)': 'TextStyle(fontWeight = FontWeight.Medium, fontSize = 12.sp, lineHeight = 16.sp, letterSpacing = 0.12.sp)',
    'TextStyle(FontWeight.Bold, 10.sp, 14.sp, letterSpacing = 1.05.sp)': 'TextStyle(fontWeight = FontWeight.Bold, fontSize = 10.sp, lineHeight = 14.sp, letterSpacing = 1.05.sp)',
}
for old, new in replacements.items():
    if old not in text:
        raise SystemExit(f'Expected typography expression missing: {old}')
    text = text.replace(old, new, 1)
path.write_text(text)
print('Named-parameter TextStyle migrations:', len(replacements))
