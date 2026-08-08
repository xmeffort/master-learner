from pathlib import Path

screen = Path('source/android/feature/home/src/main/java/com/masterlearner/feature/home/HomeScreen.kt')
text = screen.read_text()
old = '                        if (video.explanation != null) Text(video.explanation, style = MaterialTheme.typography.labelMedium, color = MaterialTheme.colorScheme.onSurfaceVariant)'
new = '                        video.explanation?.let { explanation ->\n                            Text(explanation, style = MaterialTheme.typography.labelMedium, color = MaterialTheme.colorScheme.onSurfaceVariant)\n                        }'
if old not in text:
    raise SystemExit('Expected HomeScreen nullable explanation expression missing')
screen.write_text(text.replace(old, new, 1))

vm = Path('source/android/feature/home/src/main/java/com/masterlearner/feature/home/HomeViewModel.kt')
text = vm.read_text()
old = '''    val state: StateFlow<HomeUiState> = combine(
        input,
        memory.observeDueReviewCount(),
        memory.observeSavedMomentCount(),
        telemetry.observeComprehensionProgress(),
        learnerIntelligence.snapshot,
    ) { url, reviewCount, savedCount, progress, intelligence ->
        val level = learnerSettings.snapshot.value.level
        HomeUiState.Input(
            url = url,
            dueReviewCount = reviewCount,
            savedMomentCount = savedCount,
            comprehensionProgress = progress,
            discovery = DiscoveryRanker.rank(
                candidates = discoveryRepository.curatedVideos(),
                learnerLevel = level,
                listeningEstimate = intelligence.skill(SkillDimension.LISTENING).estimate,
                vocabularyEstimate = intelligence.skill(SkillDimension.VOCABULARY).estimate,
            ),
        )
    }.stateIn(viewModelScope, SharingStarted.WhileSubscribed(5_000), HomeUiState.Input())'''
new = '''    val state: StateFlow<HomeUiState> = combine(
        input,
        memory.observeDueReviewCount(),
        memory.observeSavedMomentCount(),
    ) { url, reviewCount, savedCount ->
        HomeBaseState(url, reviewCount, savedCount)
    }.combine(telemetry.observeComprehensionProgress()) { base, progress ->
        HomeLearningState(base, progress)
    }.combine(learnerIntelligence.snapshot) { learning, intelligence ->
        val level = learnerSettings.snapshot.value.level
        HomeUiState.Input(
            url = learning.base.url,
            dueReviewCount = learning.base.reviewCount,
            savedMomentCount = learning.base.savedCount,
            comprehensionProgress = learning.progress,
            discovery = DiscoveryRanker.rank(
                candidates = discoveryRepository.curatedVideos(),
                learnerLevel = level,
                listeningEstimate = intelligence.skill(SkillDimension.LISTENING).estimate,
                vocabularyEstimate = intelligence.skill(SkillDimension.VOCABULARY).estimate,
            ),
        )
    }.stateIn(viewModelScope, SharingStarted.WhileSubscribed(5_000), HomeUiState.Input())'''
if old not in text:
    raise SystemExit('Expected HomeViewModel five-flow combine missing')
text = text.replace(old, new, 1)
marker = '@HiltViewModel\nclass HomeViewModel'
helpers = '''private data class HomeBaseState(
    val url: String,
    val reviewCount: Int,
    val savedCount: Int,
)

private data class HomeLearningState(
    val base: HomeBaseState,
    val progress: ComprehensionProgress,
)

@HiltViewModel
class HomeViewModel'''
if marker not in text:
    raise SystemExit('Expected HomeViewModel class marker missing')
vm.write_text(text.replace(marker, helpers, 1))
print('Applied Home nullable-value and typed-flow migrations')
