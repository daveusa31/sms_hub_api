template = """    {{ service_name }} = utils.Item(value="{{ service_code }}")  # {{ service_name_ }}"""

ignore_services_codes = [
    "vk", "ok", "ot", "io","ft", "yz", "hk", "yb", "uj", "wp", "qi", "sl",
    "qc", "bj", "wj", "jr", "nb", "hn", "md", "rj", "hj", "sh", "ke", "xj",
    "ll", "cy", "tk", "ki", "fs", "lf", "yk", "mg", "ya", "bd", "we", "ym"
    "qw", "pl"
]

example = """
Вконтакте	vk
Ok.ru	ok
Whatsapp	wa
Viber	vi
Telegram	tg
WeChat	wb
Google,youtube,Gmail	go
avito	av
facebook	fb
Twitter	tw
Uber	ub
Киви	qw
Gett	gt
OLX	sn
Instagram	ig
Hezzl	ss
Юла	ym
Mail.ru	ma
Microsoft	mm
Airbnb	uk
Line msg	me
Yahoo	mb
ДругВокруг	we
Пятерочка	bd
HQ Trivia	kp
Delivery Club	dt
Яндекс	ya
Steam	mt
Tinder	oi
Mamba	fd
Dent	zz
KakaoTalk	kt
AOL	pm
LinkedIN	tn
Tencent QQ	qq
Магнит	mg
pof.com	pf
Yalla	yl
kolesa.kz	kl
premium.one	po
Naver	nv
Netflix	nf
icq	iq
Onlinerby	ob
kufarby	kb
Imo	im
Michat	mc
Discord	ds
Seosprint	vv
Monobank	ji
TikTok/Douyin	lf
Ukrnet	hu
Skout	wg
EasyPay	rz
Q12 Trivia	vf
Pyro Music	ny
Wolt	rr
CliQQ	fe
ssoidnet	la
Zoho	zh
Ticketmaster	gp
Amazon	am
Olacabs	ly
Rambler	tc
ProtonMail	dp
NRJ Music Awards	pg
Citymobil	yf
MIRATORG	op
PGbonus	fx
MEGA	qr
СпортМастер	yk
Careem	ls
BIGO LIVE	bl
MyMusicTaste	mu
Snapchat	fu
Keybase	bf
OZON	sg
Wildberries	uu
BlaBlaCar	ua
Alibaba	ab
Inboxlv	iv
Nttgame	zy
Surveytime	gd
Mylove	fy
mosru	ce
Truecaller	tl
Globus	hm
Bolt	tx
Shopee	ka
Перекресток	pl
Burger King	ip
Prom	cm
AliPay	hw
Karusel	de
IVI	jc
inDriver	rl
Happn	df
RuTube	ui
Magnolia	up
Foodpanda	nz
Weibo	kf
BillMill	ri
Quipp	cc
Okta	lr
JDcom	za
MTS CashBack	da
Fiqsy	ug
KuCoinPlay	sq
Papara	zr
Wish	xv
Icrypex	cx
PaddyPower	cw
Baidu	li
Dominos Pizza	dz
paycell	xz
Lenta	rd
Payberry	qb
Drom	hz
GlobalTel	gl
Deliveroo	zk
Socios	ia
Wmaraci	xl
Yemeksepeti	yi
Nike	ew
myGLO	ae
YouStar	gb
РСА	cy
RosaKhutor	qm
eBay	dh
Квартплата+	yb
GG	qe
Grindr	yw
OffGamers	uz
Hepsiburadacom	gx
Coinbase	re
dbrUA	tj
PayPal	ts
hily	rt
SneakersnStuff	sf
Dostavista	sv
23red	qi
Blizzard	bz
ezbuy	db
CoinField	vw
Airtel	zl
YandexGo	wf
MrGreen	lw
Rediffmail	co
miloan	ey
Paytm	ge
Dhani	os
CMTcuzdan	ql
Mercado	cq
DiDi	xk
Monese	py
Kotak811	rv
Hopi	jl
Trendyol	pr
Justdating	pu
Pairs	dk
Touchance	fm
SnappFood	ph
NCsoft	sw
Tosla	nr
Ininal	hy
Paysend	tr
CDkeys	pq
AVON	ff
dodopizza	sd
McDonalds	ry
E bike Gewinnspiel	le
JKF	hr
MyFishka	qa
Craigslist	wc
Foody	kw
Grab	jg
Zalo	mj
LiveScore	eu
888casino	ll
Gamer	ed
Huya	pp
WestStein	th
Tango	xr
Global24	iz
МВидео	tk
Sheerid	rx
99app	ki
CAIXA	my
OfferUp	zm
Swvl	tq
Haraj	au
Taksheel	ei
hamrahaval	rp
Gamekit	pa
Şikayet var	fs
Getir	ul
irancell	cf
Alfa	bt
Disney Hotstar	ud
Agroinform	qu
humblebundle	un
Faberlic	rm
CafeBazaar	uo
cryptocom	ti
Gittigidiyor	nk
mzadqatar	jm
Algida	lp
Cita Previa	si
Potato Chat	fj
Bitaqaty	pt
Праймериз 2020	qc
Amasia	yo
Dream11	ve
Oriflame	qh
Bykea	iu
Immowelt	ib
Digikala	zv
Wing Money	jb
Yaay	vn
GameArena	wn
Вита экспресс	bj
Auchan	st
Picpay	ev
Blued	qn
SpotHit	cd
Brand20ua	vo
IQOS	il
Powerkredite	dx
Bisu	el
Paxful	dn
PurePlatfrom	lk
Banqi	vc
1хbet	wj
Mobile01	wk
Aitu	jj
Adidas	an
Самокат	jr
Верный	nb
Humta	gv
Divar	dw
Carousell	gj
MOMO	hc
Eneba	uf
Verse	kn
Taobao	qd
1688	hn
OnTaxi	zf
Hotline	gi
Tatneft	uc
RRSA	mn
Douyu	ak
Uklon	cp
Moneylion	qo
Apple	wx
Clubhouse	et
Nifty	px
PingPong	jh
Mailru Group	lb
Банки	md
BitClout	lt
Skroutz	sk
MapleSEA	oh
Rozetka	km
GalaxyWin	af
Ziglu	tt
Likee	jf
CityBase	az
Allegro	yn
YouGotaGift	wl
Lazada	dl
TradingView	gc
Fiverr	cn
Gabi	ou
Kwai	vp
Детский мир	rj
Yubo	uh
iQIYI	es
goods	be
Glovo	aq
IFood	pd
Quack	zw
Mocospace	gm
Dundle	fi
Switips	hg
Faceit	qz
LYKA	gz
Paysafecard	jq
Onet	ue
LightChat	xf
GoFundMe	bp
Meta	vy
JamesDelivery	ea
Столото	hj
ВкусВилл	sh
ShellBox	vg
RedBook	qf
Trip	nq
BIP	ww
Эльдорадо	ke
Whoosh	qj
KazanExpress	ol
Akulaku	tm
KeyPay	ra
СберМаркет	xj
Betfair	vd
Gojek	ni
Fastmail	mr
AliExpress	hx
Metro	bv
HandyPick	sj
ChaingeFinance	td
Iwplay	dm
GroupMe	xs
NimoTV	kz
Stripe	nu
Eyecon	kr
Lidl	pz
Twitch	hb
GalaxyChat	xe
ЗдравСити	io
Iti	ad
Setel	zg
Revolut	ij
СберАптека	sl
163СOM	wp
Hermes	en
Kaggle	zo
HeyBox	vx
Band	hl
Potato	lq
СhampionСasino	uj
Roposo	ga
Wise	bo
KFC	fz
OkCupid	vm
Pocket52	ch
Payzapp	yp
AgriDevelop	cs
CourseHero	yg
Santander	lj
Poshmark	oz
TanTan	wh
IZI	wt
Okko	og
MPL	xq
OVO	xh
Vinted	kc
4Fun	hk
Около	yz
Sizeer	eo
Букмекерские	ft
Noon	tf
WinZO	lv
Zomato	dy
DewuPoison	lx
Giftcloud	nn
Bilibili	zs
Vivo	kx
Twilio	ee
Mr Green	tp
RoyalWin	ku
Любой другой	ot
""".lstrip().rstrip()


for split_line in example.split("\n"):
    service_name, service_code = split_line.split("	")
    if service_code not in ignore_services_codes:
        rendered_template = template.replace(
            "{{ service_name }}", service_name.replace(" ", "_").upper()
        ).replace(
            "{{ service_code }}", service_code
        ).replace(
            "{{ service_name_ }}", service_name
        )

        print(rendered_template)

