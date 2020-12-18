from yargy                  import rule, and_, or_, not_
from yargy.predicates       import eq, type as _type, normalized, custom
from yargy.pipelines        import morph_pipeline
from yargy.interpretation   import fact

CityFact = fact(
    'city', 
    ['prefix', 'title']
)

CityTitle = morph_pipeline({
    'липецк', 
    'сургут', 
    'нальчик', 
    'москва', 
    'санкт-петербург', 
    'питер', 
    'нижний новгород', 
    'видное'
}).interpretation(
    CityFact.title.normalized()
)

CityRule = rule(
    normalized('город').optional().interpretation(CityFact.prefix),
    CityTitle,
    eq(';').optional()
).interpretation(
    CityFact
)
