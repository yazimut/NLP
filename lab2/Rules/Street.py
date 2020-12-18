from yargy                  import rule, and_, or_, not_
from yargy.predicates       import eq, type as _type, normalized, custom
from yargy.pipelines        import morph_pipeline
from yargy.interpretation   import fact

StreetFact = fact(
    'street',
    ['prefix', 'title']
)

StreetPrefix = morph_pipeline([
    'улица',
    'проспект', 
    'шоссе', 
    'бульвар', 
    'тракт', 
    'микрорайон', 
    'проезд', 
    'аллеи'
]).interpretation(
    StreetFact.prefix
)

StreetTitle = morph_pipeline([
    'комсомольский', 
    'катукова', 
    'рабочая', 
    'доватора', 
    'бехтеева', 
    'артема',
    'полиграфическая', 
    'каширское', 
    'октябрьский', 
    'миттова', 
    'алтуфьевское', 
    'югорская', 
    '30 лет победы', 
    'горького', 
    'крылова', 
    'хамовнический вал', 
    'парковая', 
    'пришвина', 
    'Старый Гай', 
    'школьная', 
    'юрия гагарина', 
    'гагарина', 
    'юнтоловский', 
    'меркулова', 
    'октябрьская', 
    'тюменский', 
    'олимпийский', 
    'фармана салманова', 
    'мунарева', 
    'новогиреевская', 
    'мусы джалиля', 
    'зеленые', 
    'дмитрия ульянова', 
    'маршала захарова', 
    'Кавказский', 
    'зелинского', 
    'московская', 
    'минина', 
    'береговая', 
    'кусковская', 
    'щелковское', 
    'марьинский парк', 
    '3 почтовое отделение', 
    'июльских дней', 
    'семена билецкого', 
    'антонова овсиенко', 
    'генерала армии епишева', 
    'академика байкова', 
    'подзаборного байкова', 
    'монтажника байкова', 
    'джона рида', 
]).interpretation(
    StreetFact.title
)

StreetRule = rule(
    rule(
        StreetPrefix,
        _type('RU').optional()
    ).optional(),
    StreetTitle,
    StreetPrefix.optional()
).interpretation(
    StreetFact
)
