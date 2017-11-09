import hashlib
import urllib
from django import template
from django.utils.safestring import mark_safe
import random
from django.contrib.auth.models import User

from app.models import Profile

register = template.Library()
names = """
colburnbile
fiddichclyde
xenonbadminton
tigermuffin
scuttlesdjango
knapdarlochmonty
usollie
ruincrop
loopyspine
placebosmash
calderseparately
sydneyfoshan
wrenaggravated
vestarussian
aureolegrammar
flashlightracer
eventsprincess
razorwalrus
egelwaggaford
codpiecesneak
starbummer
chockadopted
dragglewealth
advisordelay
summerfryer
citronfizz
uglyesragan
jakedpeterborough
belterbelow
unaffectedspicy
lousetackling
climatewheelhouse
maverickriley
cruiselugubrious
astronomylena
lagoscalculator
blazingsoftball
portlyburniston
gaussheader
trialsculmination
psychohindwell
tallahasseerifle
derbymacdui
protecthelicopter
controllerminute
plausiblecompare
wondermac
facebookbroom
lozengemagic
decaypreach
scallopsargue
aldebaranjittery
followedsandpiper
combinealienated
novadrummondville
stopperdessicants
farawaysphere
wiltshireenquiry
wingferrari
stainforthcommonest
shiratermite
buckinganhydrous
touringwellow
massesstanding
cherriesjiminey
peachesclink
hareshawfounded
pursescanner
curlval
titaniumtidal
punditsbogus
tyresmetacarpus
redditdeliver
zoologylist
balancedmunted
ennigparma
dollyshown
scarletrefuse
nuttermainmast
cogpaddy
switchforegoing
nerfhearderbirk
rockersscuffle
roshannasickness
sheldrakebeast
tazselawik
thermometerwhickhope
buntkietche
prevailwhipped
strippingoverhang
lustrousfur
icedcrumbly
scholarlysnollygoster
birdsbase
divergeunsuitable
dauphinetennis
strawsbadal
blaremoors
onlinedribbling
graphicask
urnpitchfork
roweryeti
chertretina
surdjeer
frontsled
teayokes
pheasantcentroid
immaterialnewlyn
frankfigurehead
mendeleviumsun
junkiecannon
cherokeemilitary
chilliwackfaced
midsedge
budgetpush
thatchedbenny
beautyswitch
goilporter
ridehondo
paellablanket
materialsenlarged
tormentedshrug
savannastudents
absentboundless
wealthpowder
mojoexpandcost
consciousport
achessyenite
opalbraces
laboredmyeloma
spatialpiston
kyrateens
upholdarid
vealbricklayer
baryonclough
creakchimpanzee
tontocomputer
buntlubberwort
cocoimaginable
slapheaddysprosium
africadummy
middleextensions
bevvyprecession
motorboatappeals
fineavaricious
caroychirm
machineplay
vestphillip
nerocabaret
topmastmultiple
bloodyblackberry
broilprecious
distraughtfiddler
pulleycricket
steepaged
tesswidespread
gunnermotion
majorbalgy
untimelyzeta
endspinwheel
heavyflair
ecozonehelmet
drowsycohesion
limitwidow
pulledvery
ladprepend
lumpishrob
tippermany
overheadsow
orogenydreaming
arrogantexpandcash
disclaimerbuzz
phalangeslovak
shroudsshelf
ananeek
kenchrabbit
farrahsoccer
decoratorsstella
smoothergucci
ligamentdhaka
bulkycici
hoffinfected
braceshark
initialscraig
parfaitautomatic
hotdogsagitta
attachedellie
bobacataract
stubbornperfumed
hygroscopiccloth
blueberriessurfer
trinketbrowed
alertpolitical
bumminankles
rageshandy
sadierow
varnishpelly
igneousclose
meecepussy
volatilemetolius
"""
NAME_LIST = names.split("\n")


# return only the URL of the gravatar
# TEMPLATE USE:  {{ email|gravatar_url:150 }}
@register.filter
def gravatar_url(email, size=150):
    url = "https://api.adorable.io/avatars/150/{}.png".format(email)
    return url

# return an image tag with the gravatar
# TEMPLATE USE:  {{ email|gravatar:150 }}
@register.filter
def gravatar(email, size=40):
    url = gravatar_url(email, size)
    return mark_safe('<img src="%s" height="%d" width="%d">' % (url, size, size))


@register.filter
def get_random_image(request):
    logos = ['12.jpg', '16.jpg', '19.jpg', '27.jpg']
    pos = random.randrange(0, 4)
    return logos[pos]


from random import randint


def get_username(id):
    num = randint(0, len(NAME_LIST))
    randid = randint(11, 99)

    full_username = str(NAME_LIST[num]) + str(randid)

    return full_username


@register.filter
def username(id):
    user = User.objects.get(pk=id)

    p, h = Profile.objects.get_or_create(user=user)
    print(p.username)
    if p.username is None:
        name = get_username(id)
        p.username = name
        p.save()
        return name
    else:
        return p.username
