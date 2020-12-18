from yargy                  import rule, and_, or_, not_
from yargy.predicates       import eq, type as _type, normalized, custom
from yargy.pipelines        import morph_pipeline
from yargy.interpretation   import fact

from .Building              import BuildingRule

AppartmentFact = fact(
    'appartment',
    ['appartment']
)

AppartmentRule = or_(
    rule(
        BuildingRule,
        _type('INT').interpretation(AppartmentFact.appartment)
    ),
    rule(
        normalized('квартира'),
        _type('INT').interpretation(AppartmentFact.appartment)
    )
).interpretation(
    AppartmentFact
)
