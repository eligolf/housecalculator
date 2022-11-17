#
# Settings for the financial calculator
# -----------------------------------------------------------------
import tempfile, base64, zlib

# Window
WIDTH = 875
HEIGHT = 760
TITLE = 'Bostadskalkylator'

ICON = zlib.decompress(base64.b64decode('eJxjYGAEQgEBBiDJwZDBy'
    'sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc='))

# Colors
WHITE = '#fff' #(255, 255, 255)
BLACK = '#000'#(0, 0, 0)
LIGHTBLUE = '#c1e7f5'
GREY = '#626262'

BG = LIGHTBLUE
FG = BLACK

# Text
ENTRY_WIDTH = 36

TITLE_FONT = 'Helvetica'
TITLE_SIZE = 12

TEXT_FONT = 'System'
TEXT_SIZE = 10

TABLE_FONT = 'Helvetica'
TABLE_SIZE = 12

OVER_TITLES = ['Allmänt', 'Hus', 'Bostadsrätt']
TITLES_ALL = ['Pris på bostad [kr]', 'Boyta [kvm]', 'Personer i hushållet', 'Storlek på lån [kr]', 'Ränta på lån [%]', 'Antal år att bo', 'Besiktning [kr]', 'Uppläggningsavgift lån [kr]', 'Mäklararvode [% eller kr]', 'Bredband [kr/mån]', 'TV/Telefoni [kr/mån]', 'Hemförsäkring [kr/mån]', 'Övriga löpande utgifter [kr/mån]']
TITLES_H = ['Värmesystem', 'Tak för fastighetsskatt [kr]', 'Storlek på existerande pantbrev [kr]', 'Underhållskostnad [kr/mån]', 'Tomträttsavgäld [kr/mån]', 'Föreningsavgifter [kr/mån]', 'Sophämtning [kr/mån]', 'Anslutningsavgift vatten/avlopp [kr/mån]', 'Hemlarm [kr/mån]']
TITLES_BR = ['Månadsavgift [kr/mån]', 'Underhållskostnad [kr/mån]']

TEXT_ALL = ['Priset som du betalar för din bostad.',
            'Storleken på inomhusarean i ditt boende.',
            'Antal personer som regelbundet bor i bostaden.',
            'Hur mycket du behöver låna till boendet. Du kan räkna ut det som priset på bostaden minus din kontantinsats.',
            'Den effektiva årsränta på lånet.',
            'Hur länge du har tänkt att bo i bostaden. Används för att räkna ut en månadskostnad för dina engångsavgifter.',
            'Vad besiktningen av boendet kostar.',
            'Vad banken har i uppläggningsavgift på ditt lån.',
            'Hur mycket mäklaren tar i avgift. Om du betalar en procent av boendekostnaden som avgift så anger du procentsatsen. Om du betalar en fast avgift så anger du avgiften i kronor.',
            'Månadskostnaden för bredband till boendet.',
            'Månadskostnaden för TV-kanaler, telefoni och övriga abonnemangskostnader.',
            'Månadskostnaden för din hemförsäkring.',
            'Om du har fler avgifter som du vill ta med i beräkningen så anger du månadskostnaden för dessa här.']
TEXT_H = ['Ange vilket sorts värmesystem som finns. Detta används för att beräkna uppvärmningskostnaden för ditt boende.',
          'Alla som äger en fastighet behöver betala fastighetsskatt. Du betalar 0.75% av taxeringsvärdet på fastigheten, men aldrig mer än 7 812 kronor per bostadsbyggnad (tak för år 2019).',
          'Banken tar ut en säkerhet för lånet, ett så kallat pantbrev. Kostnaden för detta är en fast avgift på 375 kr plus 2% av storleken på lånet, minus redan existerande pantbrev, dvs: 375 + 0.02 x (storlek_lån - existerande_pantbrev). I detta fält anger du storleken på de pantbrev som redan finns på bostaden.',
          'Här räknas på hur mycket som sätts undan för underhållsarbete per månad. Underhållskostnaden för ett hus inkluderar underhåll av fasad, köp av vitvaror och övriga renoveringar. Värdet 2 167 kr/mån kommer från en rekommendation från Nordea om att sätta av 26 000 kr/år för underhåll.',
          'Ofta ägs huset, men inte marken som huset står på. För att utnyttja marken betalas därför en tomträttsavgäld till markägaren (ofta kommunen). Denna avgift varierar kraftigt, justera därför detta fält för att matcha det boende du räknar på.',
          'Ibland förekommer föreningsavgifter som inkluderar parkering, städning och liknande. Finns det sådana avgifter för ditt boende så fyller du i dem här.',
          'Den förifyllda avgiften baseras på en årsavgift på 1 750 kronor för sophämtning. Ändra om detta inte stämmer för ditt boende.',
          'Den förifyllda avgiften baseras på en årsavgift på 2 100 kronor för anslutning av vatten och avlopp. Ändra om detta inte stämmer för ditt boende.',
          'Om ditt boende har hemlarm så fyller du i månadskostnaden för det här.']
TEXT_BR = ['På samma sätt som hyresgäster betalar hyra för sitt boende måste du som har en bostadsrätt betala en månadsavgift till bostadsrättsföreningen. Denna avgift framgår på annonsen för boendet.',
           'Här räknas på hur mycket som sätts undan för underhållsarbete per månad. Underhållskostnaden för en bostadsrätt är lägre än för ett hus, då de flesta yttre reparationer och renoveringar bekostas av bostadsrättsföreningen. En schablonavgift för att täcka inre renoveringar, köp av vitvaror och liknande är här satt till 1 000 kr/mån. Om du har en ny bostadsrätt kan du minska kostnaden men om du har en äldre bostadsrätt som är i behov av renoveringar så kan avgiften behöva ökas.']

# Pre-defined fields (from: http://hushuvud.se/driftkostnad-hus/)
PRICE_ = 2000000
PRICE_H_ = 3000000

DEPOSIT_ = 1400000
DEPOSIT_H_ = 2400000

MAINTENANCE_ = 1000
MAINTENANCE_H_ = round(26000/12)

ALARM_ = 0 
ALARM_H_ = 0

SPACE_ = 80
ANTAL_ = 2
INTEREST_ = 5.5
INTERESTPRICE_ = 300
PANT_ = 0
TAXROOF_ = 7812
CHECKUP_ = 10000
BROKER_ = 4
YEARS_ = 10
BROADBAND_ = 450
TOMTGALD_ = 1000
FORENING_ = 0
TV_ = 400
FORSAKRING_ = 150
AVGIFT_ = 2500
NETTOSKULD_ = 55
GARBAGE_ = 145
WATER_ = 175
ANDELSTAL_ = 2
OVRIGT_ = 0
SKULDKVOT_ = 7.5 # https://sustend.se/dubbel-rantesmall-for-dig-med-bostadsratt/
