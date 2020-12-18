from yargy                  import rule, and_, or_, not_
from yargy.predicates       import eq, type as _type, normalized, custom
from yargy.pipelines        import morph_pipeline
from yargy.interpretation   import fact

from .Street                import StreetRule

BuildingFact = fact(
    'building',
    ['house', 'corpus', 'structure']
)

HouseNumber = rule(
    _type('INT'),
    rule(or_(
        rule(
            eq('/'),
            _type('INT')
        ),
        rule(custom(lambda token: len(token) == 1))
    )).optional()
).interpretation(
    BuildingFact.house
)

House = rule(
    rule(or_(
        StreetRule,
        rule(
            normalized('дом').repeatable(),
            normalized('номер').optional(),
        )
    )),
    HouseNumber
)

CorpusPrefix = morph_pipeline([
    'корпус', 
    'к'
])

Corpus = rule(
    CorpusPrefix,
    _type('INT').interpretation(BuildingFact.corpus)
)

StructurePrefix = morph_pipeline([
    'строение', 
    'ст'
])

Structure = rule(
    StructurePrefix,
    _type('INT').interpretation(BuildingFact.structure)
)

BuildingRule = rule(
    House,
    Corpus.optional(),
    Structure.optional()
).interpretation(
    BuildingFact
)
