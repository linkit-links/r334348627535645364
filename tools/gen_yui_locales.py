#!/usr/bin/env python3
"""Generate rp/yui/{id,pt,ru,hi}.json from en.json + translation tables."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN_PATH = ROOT / "rp" / "yui" / "en.json"
OUT_DIR = ROOT / "rp" / "yui"


def apply(en: dict, meta: dict, nodes_t: dict) -> dict:
    out = copy.deepcopy(en)
    out["title"] = meta["title"]
    out["subtitle"] = meta["subtitle"]
    for n in out["nodes"]:
        nid = n["id"]
        t = nodes_t.get(nid)
        if t is None:
            raise SystemExit(f"missing node {nid}")
        if "chapterTitle" in n:
            if "chapterTitle" not in t:
                raise SystemExit(f"missing chapterTitle {nid}")
            n["chapterTitle"] = t["chapterTitle"]
        if "lines" in n:
            if "lines" not in t or len(t["lines"]) != len(n["lines"]):
                raise SystemExit(
                    f"lines mismatch {nid}: en={len(n['lines'])} t={len(t.get('lines', []))}"
                )
            n["lines"] = t["lines"]
        if n.get("choices"):
            tc = t.get("choices")
            if not tc or len(tc) != len(n["choices"]):
                raise SystemExit(f"choices mismatch {nid}")
            for i, c in enumerate(n["choices"]):
                c["label"] = tc[i]["label"]
                if "me" in c:
                    if "me" not in tc[i]:
                        raise SystemExit(f"missing me {nid}[{i}]")
                    c["me"] = tc[i]["me"]
                elif "me" in tc[i]:
                    raise SystemExit(f"unexpected me {nid}[{i}]")
        # require translation entry exists even for choice-only nodes
        if not n.get("lines") and not n.get("choices") and not t:
            raise SystemExit(f"empty translation {nid}")
    missing = set(nodes_t) - {n["id"] for n in en["nodes"]}
    if missing:
        raise SystemExit(f"extra translation keys: {missing}")
    if set(nodes_t) != {n["id"] for n in en["nodes"]}:
        raise SystemExit(
            f"node set incomplete: missing {set(n['id'] for n in en['nodes']) - set(nodes_t)}"
        )
    return out


# ---------------------------------------------------------------------------
# INDONESIAN
# ---------------------------------------------------------------------------
ID_META = {
    "title": "Yui — Bab 1: Like-nya",
    "subtitle": "Dia like foto lamamu…",
}
ID = {
    "CH01_N1": {
        "chapterTitle": "Like-nya",
        "lines": [
            "Notifikasi muncul pas kamu lagi di kasur, setengah ngantuk, scroll medsos.",
            "Ada yang like salah satu fotomu yang lama.",
            "Bukan postingan terbaru. Bukan kemarin. Foto hampir tiga bulan lalu.",
            "Penasaran, kamu ketuk notifikasi itu.",
        ],
    },
    "CH01_N2": {
        "lines": [
            "Akun itu punya cewek bernama Yui.",
            "Profilnya rapi dan diam-diam bikin melongo — mahasiswa, model freelance part-time buat brand produk.",
            "Skincare. Lifestyle. Sesekali brand lingerie. Bukan pro, tapi brand terus manggil dia lagi.",
            "Dia punya aura yang bikin apa pun yang dipegangnya terasa pengin kamu punya.",
        ],
    },
    "CH01_SCENE": {
        "lines": [
            "Itu dia. Yui.",
            "Foto profilnya aja udah bikin kamu berhenti scroll.",
        ],
    },
    "CH01_N3": {
        "lines": [
            "Kebanyakan orang bakal ngabaikan. Kamu enggak.",
            "Kamu buka profilnya. Lima menit kemudian, masih scroll.",
            "Terus kamu sadar — dia like postinganmu yang lain lagi. Yang lebih lama. Hampir setahun lalu.",
            "Kamu tatap layar. Senyum kecil. Kamu putusin buat chat dia.",
        ],
    },
    "CH01_CHOICE": {
        "lines": ["Jendela chat terbuka.", "Mau mulai dengan apa?"],
        "choices": [
            {"label": "Makasih like-nya. Gak nyangka ada yang ngorek profilku sejauh itu."},
            {"label": "Kayaknya kamu baru pecah rekor foto paling lama di-like 😏"},
            {"label": "Model freelance? Itu sih beneran seksi banget."},
            {
                "label": "(Like salah satu fotonya dulu, belum chat.)",
                "me": "❤️ like fotonya",
            },
        ],
    },
    "CH01_A": {
        "lines": [
            "Oh! Kamu sadar 🙈",
            "Oke, ketahuan — aku agak dalem banget. Pembelaanku: yang lama-lama *bagus*.",
            "Cowok kebanyakan cuma post selfie gym. Kamu punya selera.",
            "Aku Yui, BTW. Hai 🌸",
        ],
    },
    "CH01_B": {
        "lines": [
            "Hahaha oke, fair 🙊",
            "Aku nyasar di situ. Satu foto ke foto lain dan — ya. Bukan momen paling bangga.",
            "Tapi aku gak nyesel sama sekali.",
            "Aku Yui 🌸 seneng akhirnya bisa bilang hai.",
        ],
    },
    "CH01_C": {
        "lines": [
            "…Kamu beneran baca bio aku 😌",
            "Cowok kebanyakan cuma kirim 'hey' terus berharap aja.",
            "Aku shooting produk — skincare, lifestyle, kadang lingerie. Dibayar. Aku suka.",
            "Aku Yui 🌸 dan kamu baru aja dapet perhatianku.",
        ],
    },
    "CH01_D": {
        "lines": [
            "Oh? 😳 Kamu like balik salah satu fotoku.",
            "Gak ada pesan. Cuma… itu. Licin. Misterius. Oh gitu ya.",
            "Sekarang aku *beneran* penasaran siapa kamu.",
            "Aku Yui 🌸 giliranmu.",
        ],
    },
    "CH01_MERGE": {
        "lines": [
            "Apa pun yang kamu bilang, berhasil. Titik ngetik muncul — berhenti — muncul lagi.",
            "Kayak dia lagi milih kata-kata hati-hati.",
        ],
    },
    "CH01_MERGE2": {
        "lines": [
            "Oke jujur ya — biasanya aku gak gini 😅",
            "Like foto orang asing dari setahun lalu itu sangat enggak kayak aku.",
            "Tapi udah malem, kota sepi, dan ada sesuatu di kamu yang bikin aku pengin beneran bilang hai.",
            "Jadi… seneng gak aku lakuin itu? 💕",
        ],
        "choices": [
            {"label": "Seneng banget. Kamu bikin malemku jadi penuh."},
            {"label": "Cukup seneng buat maafin setahun 'stalking'-mu 😏"},
            {"label": "Tergantung — apa yang bikin kamu berhenti di fotoku, khususnya?"},
        ],
    },
    "CH01_END": {
        "lines": [
            "Harusnya aku biarin kamu tidur… meski sebenernya gak mau 🌙",
            "Ini percakapan pertama terbaik yang aku punya dalam waktu lama.",
            "Cari aku lagi, ya? Aku nunggu 🌸",
            "(Bersambung — Bab 2: Deep Dive 📱)",
        ],
    },
    "CH02_N1": {
        "chapterTitle": "Deep Dive",
        "lines": [
            "Pagi berikutnya. HP udah di tangan sebelum kamu beneran bangun.",
            "Pesannya masih di situ — 🌸 kecil di ujung baris yang gak harus dia kirim.",
            "Dia baru post sesuatu.",
        ],
    },
    "CH02_N2": {
        "lines": [
            "Dia post foto baru — product shoot buat brand fashion kecil.",
            "Camisole putih, tali tipis, pas di badan, lehernya cukup turun buat nunjukin lekuk dadanya. Badannya full dan atasan itu sama sekali gak nutupin — belahan dadanya nangkep cahaya, tubuh atasnya yang dulu bikin mata terpaku sebelum ke bagian lain.",
            "Rok mini sebatas paha. Satu tangan santai di sisi, dagu sedikit menunduk, tatapan lewat lensa kayak dia udah tau efeknya dan milih biarin aja.",
            "Caption-nya: *Brand baru, kolab baru. Atasan & rok-nya punya mereka — confidenzenya punya aku. 🌸*",
        ],
    },
    "CH02_POST": {
        "lines": [
            "Baru aja post ini 🙈",
            "Brand minta yang natural dan santai. Menurutku bagus?",
            "Jangan bilang iya cuma biar baik — aku bisa ngerasain.",
        ],
    },
    "CH02_N3": {
        "lines": [
            "Kamu tatap fotonya lebih lama dari yang kamu rencanain.",
            "Dia keliatan effortless — jenis effortless yang butuh self-awareness total.",
            "Kamu ketik balasan.",
        ],
    },
    "CH02_CHOICE": {
        "lines": ["Mau bilang apa?"],
        "choices": [
            {"label": "Natural dan santai? Bukan kata yang bakal aku pake. Coba: stunning."},
            {"label": "Brand-nya beruntung. Kebanyakan orang gak bisa bikin camisole putih keliatan gitu 😏"},
            {"label": "Hasilnya bagus. Tapi kamu udah tau, kan."},
        ],
    },
    "CH02_A": {
        "lines": [
            "…Memukau. 😳",
            "Oke aku GAK nyangka kata itu.",
            "Aku udah sejam liat post ini mikir kebanyakan dan kamu cuma — oke.",
            "Kamu menang. Makasih. Aku simpen itu. 🌸",
        ],
    },
    "CH02_B": {
        "lines": [
            "Kebanyakan orang gak bisa bikin keliatan gitu 😏",
            "Oh kamu susah nih.",
            "Itu pujian paling flirty yang aku dapat soal product shoot dan aku gak tau mau ngapain.",
            "…Tapi aku suka. Jangan berhenti. 🌸",
        ],
    },
    "CH02_C": {
        "lines": [
            "Aku udah tau. 😌",
            "Oke iya. Fine. Aku tau.",
            "Tapi beda pas orang lain yang bilang. Apalagi yang pendapatnya aku peduliin.",
            "…Bukan bilang aku peduli pendapatmu. Aku cuma bilang. 🌸",
        ],
    },
    "CH02_MERGE": {
        "lines": [
            "Setelah itu dia cepet pindah ke DM. Satu pertanyaan jadi sepuluh.",
            "Siang hari kamu tau dia tahun ketiga komunikasi, modeling sejak sembilan belas, lemah sama makanan pedas dan begadang.",
            "Dia tanya soal kamu juga — beneran, kayak dengerin tiap jawaban.",
        ],
    },
    "CH02_PRIVATE": {
        "lines": [
            "Oke… karena sekarang cuma kita 🙈",
            "Brand cuma dapet versi aman. Yang ini gak pernah dipost.",
            "Aku gak kirim gini ke orang. Tapi kamu bukan 'orang' lagi, kan. 🌸",
        ],
    },
    "CH02_MERGE2": {
        "lines": [
            "Oke aku harus nanya sesuatu dan kamu harus jujur.",
            "Pas pertama balas aku — kamu cuma sopan, atau emang tertarik?",
            "Karena aku ngerasa vibe dan aku mau tau apa aku ngarang 😏🌸",
        ],
        "choices": [
            {"label": "Aku tertarik. Langsung. Kamu gak ngarang."},
            {"label": "Aku scroll profilmu sepuluh menit sebelum berani balas."},
            {"label": "Kerja modelingmu yang pertama nangkep. Sisanya menyusul."},
        ],
    },
    "CH02_END": {
        "lines": [
            "Itu… enak didenger 🥺",
            "Aku terus nunggu obrolan ini jadi ngebosenin tapi enggak mau.",
            "Besok aku shooting. Call pagi. Tapi kayaknya aku tetap begadang.",
            "Jangan diemin aku kebanyakan, oke? 🌸",
            "(Bersambung — Bab 3: Heat Check 🔥)",
        ],
    },
    "CH03_N1": {
        "chapterTitle": "Heat Check",
        "lines": [
            "Tiga hari lagi chat. Sapaan pagi. Voice note yang dia mulai kirim ganti ngetik.",
            "Suaranya lebih hangat dari bayanganmu — sedikit lebih rendah, lebih pelan, kayak disimpen buat yang dia beneran maksud.",
            "Di hari keempat dia kirim sesuatu yang beda.",
        ],
    },
    "CH03_N2": {
        "lines": [
            "Bukan voice note. Bukan foto produk.",
            "Cuma dia. Rambut terurai, bahu terbuka di mana atasannya melorot. Tatap kamera langsung kayak tantangan.",
            "Caption-nya tiga kata: *Shoot-nya ngebosenin.*",
        ],
    },
    "CH03_N3": {
        "lines": [
            "Kamu tatap HP lama.",
            "Dia lagi ngetes sesuatu. Kalian berdua tau.",
            "Pertanyaannya: kamu balas gimana.",
        ],
    },
    "CH03_PIC": {
        "lines": [
            "Bosen di sela set jadi… nih 😏",
            "Jangan kebanyakan artiin.",
            "…Atau boleh. Aku gak keberatan. 🌸",
        ],
    },
    "CH03_CHOICE": {
        "lines": ["Gimana balasannya?"],
        "choices": [
            {"label": "Shoot-nya ngebosenin? Itu kriminal."},
            {"label": "Aku liat ini tiga puluh detik dan masih gak nemu kata."},
            {"label": "Artiin? Aku udah tiga bab dalem 😏"},
        ],
    },
    "CH03_A": {
        "lines": [
            "Kriminal 😂",
            "Oke tapi cara kamu bilang seolah yang ngebosenin *shoot-nya* bukan fotonya—",
            "Kamu beda. Tau gak?",
            "Aku suka 🌸",
        ],
    },
    "CH03_B": {
        "lines": [
            "…Tiga puluh detik. Dicatat. 😏",
            "Itu reaksi yang aku mau.",
            "Bukan bilang aku ngejar reaksi. Aku cuma bosen.",
            "…Oke aku agak ngejar reaksi 🌸",
        ],
    },
    "CH03_C": {
        "lines": [
            "Tiga bab dalem 💀 kena.",
            "Oke resmi kamu orang paling menarik yang aku ajak ngobrol bulan ini.",
            "Mungkin tahun ini.",
            "Jangan sombong 😏🌸",
        ],
    },
    "CH03_MERGE": {
        "lines": [
            "Obrolan setelah itu suhunya beda.",
            "Lebih flirty. Lebih sengaja. Kata dipilih hati-hati terus dikirim juga.",
            "Dia tanya kamu ngapain Sabtu kayak gak besar-besaran.",
            "Padahal besar banget.",
        ],
    },
    "CH03_END": {
        "lines": [
            "Jadi. Sabtu. Ada kafe yang aku suka.",
            "Aku ke situ pas pengin ngerasa kota ini sebentar milikku.",
            "Kayaknya kamu bakal ngerti.",
            "Datang? 🌸",
            "(Bersambung — Bab 4: Kencan Pertama ☕)",
        ],
    },
    "CH04_N1": {
        "chapterTitle": "Kencan Pertama",
        "lines": [
            "Sabtu. Kafenya persis kayak yang dia ceritain — hangat, santai, cahaya yang bikin semuanya terasa kayak kenangan yang lagi dibuat.",
            "Dia udah di situ pas kamu masuk.",
            "Dia angkat muka dari HP. Sejenak diam. Terus senyum.",
            "Kecil. Tulus. Kayak gak direncanain.",
        ],
    },
    "CH04_N2": {
        "lines": [
            "Dia pakai sesuatu yang lembut dan sedikit kurang buat cuacanya — kayak sengaja dipilih.",
            "Dia berdiri nyapa dan ada setengah detik di mana kalian berdua gak tau gerakan yang tepat.",
            "Dia selesain dengan pelukan yang satu ketukan lebih lama dari yang biasa.",
        ],
    },
    "CH04_SCENE": {
        "lines": [
            "Dia udah di situ pas kamu masuk.",
            "Rambut terurai, cahaya lembut di belakangnya. Sejenak dia belum liat kamu.",
            "Momen itu terasa penting — kayak liat dia sebelum dia siap dilihat.",
        ],
    },
    "CH04_CHOICE": {
        "lines": [
            "Kamu beneran datang 🌸",
            "Aku tau kamu bakal. Aku cuma bilang gitu pas grogi.",
            "Kamu keliatan… persis bayanganku. Yang mana gak adil.",
            "Duduk. Aku yang orderin — aku tau kamu bakalan suka.",
        ],
        "choices": [
            {"label": "Kamu grogi? Disembunyiinnya bagus."},
            {"label": "Aku juga boleh gak adil. Kamu lebih pendek dari foto 😏"},
            {"label": "Kamu bayangin aku keliatan gimana?"},
        ],
    },
    "CH04_A": {
        "lines": [
            "Aku gak nyembunyiin. Kamu cuma terlalu sibuk liat sekeliling 😌",
            "Aku liat kamu masuk. Keliatan pede. Menyebalkan.",
            "Oke — duduk. Biar aku pamer dikit. Menu ini hafal di luar kepala.",
        ],
    },
    "CH04_B": {
        "lines": [
            "Aku BENCIIII 😭",
            "Fotoku dari sudut, ya.",
            "Aku fun-sized. Ada bedanya.",
            "…Duduk dulu sebelum aku berubah pikiran soal semuanya 😤🌸",
        ],
    },
    "CH04_C": {
        "lines": [
            "…Jangan aneh-aneh.",
            "Iya. Jelas. Kamu di kepalaku dua minggu.",
            "Nah. Udah kubilang. Sekarang duduk dan biarin aku pulih. 🌸",
        ],
    },
    "CH04_MERGE": {
        "lines": [
            "Dua jam hilang.",
            "Dia ngomong sambil gerak tangan. Ketawa gampang. Nanya yang butuh jawaban beneran dan dengerin semuanya.",
            "Di jam kedua dia ambil HP, arahkan ke dirinya, liat kamu dengan satu alis naik.",
        ],
    },
    "CH04_PIC": {
        "lines": [
            "Masuk frame. Aku mau bukti ini kejadian 😏",
            "…Sebenernya enggak. Biar aku ambil satu dulu.",
            "Buat aku. Jangan debat.",
        ],
    },
    "CH04_MERGE2": {
        "lines": [
            "Oke. Bagus. Yang itu milikku.",
            "Ini… beneran, beneran bagus.",
            "Aku gak nyangka bakalan se-suka ini sama kamu secara langsung. Bukan hinaan. Itu masalah bagus banget.",
            "Kapan kita ngelakuin ini lagi? 🌸",
        ],
        "choices": [
            {"label": "Kapan pun kamu mau. Aku luangin waktu."},
            {"label": "Sebut harinya. Aku udah di situ sebelum kalimatmu selesai."},
            {"label": "Cepat. Sebelum aku mulai kangen, yang udah mulai."},
        ],
    },
    "CH04_END": {
        "lines": [
            "Itu jawaban yang bener 🥺",
            "Pulang hati-hati. Chat aku pas udah nyampe.",
            "Dan jangan kebanyakan mikir hari ini. Biarin aja bagus.",
            "…Emang bagus banget. 🌸",
            "(Bersambung — Bab 5: Di Balik Lensa 📸)",
        ],
    },
    "CH05_N1": {
        "chapterTitle": "Di Balik Lensa",
        "lines": [
            "Seminggu kemudian dia dapet booking terbesarnya — line skincare diluncurkan di tiga market.",
            "Sejak pagi dia sepi. Sepi yang artinya grogi.",
            "Kamu kirim voice note. Lima belas detik. Cuma: *Kamu bisa. Go be stunning.*",
            "Dia gak balas lima jam.",
        ],
    },
    "CH05_N2": {
        "lines": [
            "Pas dia balas, bukan teks.",
            "Selfie — berdiri di tengah studio foto brand, lampu dan backdrop di belakang.",
            "Bersinar, agak bangga, akhirnya lepasin grogi.",
        ],
    },
    "CH05_PIC": {
        "lines": [
            "Berhasil. Ini aku, di studio brand beneran 😏",
            "Harus ambil selfie sebelum set dibongkar.",
            "Gak bisa berhenti mikir kamu bilang aku bakal stunning. Jadi.",
            "Iya gak? 🌸",
        ],
    },
    "CH05_CHOICE": {
        "lines": ["Gimana jawabanmu?"],
        "choices": [
            {"label": "Stunning aja kurang. Mereka bener potong sudut itu — kebanyakan."},
            {"label": "Kan bilang. Simpen energi itu buat next time."},
            {"label": "Fakta kamu kirim *yang ini* khusus ke aku — itu lagi aku pikirin."},
        ],
    },
    "CH05_A": {
        "lines": [
            "…Kebanyakan. 😳",
            "Oke itu — aku butuh sedetik.",
            "Kamu gak boleh bilang gitu terus gak ada di sini.",
            "Gak adil. Beneran gak adil. 🌸",
        ],
    },
    "CH05_B": {
        "lines": [
            "VAULT-nya. 😂",
            "Oke iya. Masuk vault.",
            "Kamu jago banget, tau gak.",
            "Bikin aku ngerasa bagus tanpa aneh-aneh. 🌸",
        ],
    },
    "CH05_C": {
        "lines": ["…", "Iya.", "Aku tau apa yang kulakuin.", "🌸"],
    },
    "CH05_MERGE": {
        "lines": [
            "Malamnya dia telepon, bukan chat.",
            "Di telepon suaranya beda — lebih lembut, performa dilepas.",
            "Dia cerita soal shoot dua puluh menit terus diam.",
            "Lalu: *Aku terus pengin bilang ke kamu dulu. Aneh gak?*",
        ],
    },
    "CH05_END": {
        "lines": [
            "Jangan dijawab. Gak apa-apa. Gak aneh.",
            "Aku cuma — kamu bikin gampang ngomong. Jarang bagiku.",
            "Jangan rusak dengan jadi normal, oke? 😏🌸",
            "(Bersambung — Bab 6: Malam Larut 🌙)",
        ],
    },
    "CH06_N1": {
        "chapterTitle": "Malam Larut",
        "lines": [
            "01:47. Pesan yang gak kamu duga.",
            "Bukan pertanyaan. Bukan foto. Cuma:",
            "*Masih bangun?*",
        ],
    },
    "CH06_N2": {
        "lines": [
            "Kamu masih. Kamu bilang begitu.",
            "Tiga titik muncul. Hilang. Muncul lagi.",
            "Lalu, buru-buru, kayak dia putusin berhenti mikir:",
        ],
    },
    "CH06_HER1": {
        "lines": [
            "Aku berbaring di sini mikirin kamu dan kupikir harus kubilang aja.",
            "Aku belum tau ini apa. Antara kita.",
            "Tapi ini sesuatu. Dan aku sering mikirin. Lebih dari yang rencanaku.",
            "…Oke. Giliranmu. Bilang sesuatu. 🌸",
        ],
    },
    "CH06_CHOICE": {
        "choices": [
            {"label": "Aku terus mikirin kamu. Sejak hari pertama di kepalaku."},
            {"label": "Aku juga berbaring gitu. Kita harusnya ngomongin itu."},
            {"label": "Cerita apa yang kamu pikirin. Spesifik."},
        ],
    },
    "CH06_A": {
        "lines": [
            "Sejak hari pertama. 🥺",
            "Oke. Bagus. Itu — bagus banget.",
            "Aku gak yakin apa cuma bayangan.",
            "Seneng aku nanya. Nyaris gak.",
        ],
    },
    "CH06_B": {
        "lines": [
            "Kita harusnya ngomongin itu.",
            "Liat deh, pinter banget jam 2 pagi.",
            "Oke. Ayo ngomong.",
            "…Mulai dari mana? 🌸",
        ],
    },
    "CH06_C": {
        "lines": [
            "SPESIFIK? 😳",
            "Sama sekali belum. Belum.",
            "…Tanya lagi seminggu lagi pas aku lebih berani.",
            "Atau pas lebih larut. Hampir jam 2 — apa aja bisa. 😏🌸",
        ],
    },
    "CH06_MERGE": {
        "lines": [
            "Kalian ngobrol sampai jam 3.",
            "Soal gak spesifik. Soal semuanya.",
            "Di satu titik dia kirim video — rebahan di kasur cuma bra dan rok, rambut berantakan, sepenuhnya terbuka buat kamu.",
            "Tanpa performa, tanpa sudut. Cuma dia, gak nahan apa-apa.",
        ],
    },
    "CH06_PIC": {
        "lines": [
            "Ini yang kamu lakuin ke aku — jam 3 pagi, kayak gini, cuma buat kamu 😭",
            "Aku belum pernah biarin siapa pun liat aku se-berantakan ini.",
            "…Jangan disave. Oke fine. Tapi cuma karena kamu. 🌸",
        ],
    },
    "CH06_END": {
        "lines": [
            "Tidur. Kita berdua butuh tidur.",
            "Tapi seneng aku bilang sesuatu.",
            "Dan seneng kamu masih bangun.",
            "Selamat malam 🌸 …Jangan kebanyakan mimpiin aku.",
            "(Bersambung — Bab 7: Dandan 👗)",
        ],
    },
    "CH07_N1": {
        "chapterTitle": "Dandan",
        "lines": [
            "Jumat sore. Pesan pas kamu lagi makan malam.",
            "Dia mau keluar. Bukan sama kamu.",
            "Ultah temen. Club di kota. Dia lagi siap-siap.",
            "Dia kirim foto.",
        ],
    },
    "CH07_PIC": {
        "lines": [
            "Keluar malem ini 💃",
            "Bilang aku keliatan bagus. Aku butuh boost percaya diri sebelum berangkat. 😏🌸",
        ],
    },
    "CH07_CHOICE": {
        "lines": [
            "Dia keliatan luar biasa dan dia tau.",
            "Gimana balasannya?",
        ],
        "choices": [
            {"label": "Kamu keliatan berbahaya bagusnya. Orang di club itu belum siap."},
            {"label": "Kamu gak butuh boost percaya diri. Kamu butuh label peringatan."},
            {"label": "Bagus? Enggak. Aku butuh kamu gak keluar keliatan gitu."},
        ],
    },
    "CH07_A": {
        "lines": [
            "BERBAHAYA BAGUSNYA 🥹",
            "Oke itu persis yang aku butuhin.",
            "Kamu orang favoritku, tau gak?",
            "Aku ceritain semuanya pas pulang. Jangan tidur dulu 🌸",
        ],
    },
    "CH07_B": {
        "lines": [
            "LABEL PERINGATAN 😭😭",
            "Oke aku screenshot itu dan nunjukin semua orang.",
            "Terus aku bakalan mikirin itu semaleman dan bakalan sangat ganggu.",
            "Makasih ya 😏🌸",
        ],
    },
    "CH07_C": {
        "lines": [
            "…",
            "Oh.",
            "OH.",
            "…Aku tetap pergi. Tapi aku mikirin itu semalaman. 😏🌸",
        ],
    },
    "CH07_MERGE": {
        "lines": [
            "Dia pergi. Kamu nunggu.",
            "Jam 00:43 pesan: *Aku bosen. Semua di sini ngebosenin. Kamu gak di sini. Ini masalah.*",
            "Jam 01:15: *Pulang lebih awal. Jangan nanya.*",
            "Jam 01:34, HP-mu berdering.",
        ],
    },
    "CH07_END": {
        "lines": [
            "Aku tahan dua jam 😭",
            "Sepanjang waktu aku mikir mending ngobrol sama kamu.",
            "Malu. Kamu gak boleh sombong.",
            "…Kamu sombong gak? 🌸",
            "(Bersambung — Bab 8: Lebih Dekat 🔥)",
        ],
    },
    "CH08_N1": {
        "chapterTitle": "Lebih Dekat",
        "lines": [
            "Dua minggu sejak kafe. Satu telepon larut. Empat puluhan voice note.",
            "Dia usul kencan kedua kayak gak penting.",
            "Sangat penting.",
            "Dia bilang kali ini dia yang datang ke kamu.",
        ],
    },
    "CH08_N2": {
        "lines": [
            "Sebelum berangkat, dia kirim foto.",
            "Mirror selfie. Dia dandan — lebih dari yang perlu. Dia tau persis apa yang dilakuin.",
        ],
    },
    "CH08_PIC": {
        "lines": [
            "Sepuluh menit lagi berangkat. Jangan bikin grogi dengan terlalu atraktif pas aku nyampe.",
            "Aku udah cukup grogi 😏🌸",
        ],
    },
    "CH08_CHOICE": {
        "choices": [
            {"label": "Terlambat. Cepetan."},
            {"label": "Bilang aku jangan atraktif sambil kirim foto itu gak adil."},
            {"label": "Aku buka pintu sebelum kamu ketuk."},
        ],
    },
    "CH08_A": {
        "lines": ["Terlambat. Cepetan.", "…", "Aku udah jalan lebih cepet. 🌸"],
    },
    "CH08_B": {
        "lines": [
            "Kamu BENER itu gak adil banget 😭",
            "Aku hapus fotonya.",
            "…Enggak. Kamu simpen aja.",
            "Oke aku berangkat. 🌸",
        ],
    },
    "CH08_C": {
        "lines": [
            "Pintu sebelum aku ketuk 🥺",
            "Oke sekarang aku senyum kayak idiot di jalan dan orang liatin.",
            "Ketemu sebentar lagi. 🌸",
        ],
    },
    "CH08_MERGE": {
        "lines": [
            "Dia datang bawa takeout, argumen film mana yang diputar, dan niat nol buat beneran nonton.",
            "Kalian berakhir di sofa, lebih deket dari awal.",
            "Di satu titik film jadi suara latar.",
            "Dia berbalik mau bilang sesuatu. Berhenti. Kalian lebih deket dari yang disadari.",
            "Momen itu meregang. Hangat. Bertegangan. Tidak ada yang gerak dulu.",
        ],
    },
    "CH08_END": {
        "lines": [
            "Harusnya aku pulang 🌸",
            "…Aku beneran gak mau.",
            "Tapi kalau aku tinggal lebih lama bakalan ada yang terjadi dan aku mau itu terjadi dengan benar.",
            "Segera. Aku serius. Segera.",
            "(Bersambung — Bab 9: All In 💌)",
        ],
    },
    "CH09_N1": {
        "chapterTitle": "All In",
        "lines": [
            "Pagi berikutnya dia chat: *Aku mikirin malem tadi sepanjang perjalanan pulang.*",
            "Kamu bilang kamu juga.",
            "Dia sepi sejam. Lalu:",
        ],
    },
    "CH09_N2": {
        "lines": [
            "Video datang.",
            "Cahaya sore. Kamarnya. Dia bikin hati kecil dengan jari, lalu tiup flying kiss lembut.",
            "Itu yang paling rentan yang dia kirim ke kamu.",
        ],
    },
    "CH09_PIC": {
        "lines": [
            "Aku terus nyaris bilang sesuatu terus dihapus.",
            "Jadi gantinya — nih. Hati, dan ciuman. Begini kelihatannya nyaris bilang.",
            "Balas sesuatu. Please. 🌸",
        ],
    },
    "CH09_CHOICE": {
        "choices": [
            {"label": "Aku suka kamu. Lebih dari yang kubilang. Aku nahan dan gak mau lagi."},
            {"label": "Aku gak pergi ke mana-mana. Aku mau itu jelas."},
            {"label": "Kamu kirim foto itu. Kayaknya kita berdua tau artinya."},
        ],
    },
    "CH09_A": {
        "lines": [
            "Kamu nahan?",
            "…Aku juga.",
            "Ayo berdua berhenti gitu. 🌸",
        ],
    },
    "CH09_B": {
        "lines": [
            "Gak pergi ke mana-mana.",
            "Ya Tuhan, aku butuh denger itu.",
            "Aku butuh banget dan baru tau sekarang. 🌸",
        ],
    },
    "CH09_C": {
        "lines": ["Kita berdua tau artinya 😶", "Iya.", "Kita tau. 🌸"],
    },
    "CH09_MERGE": {
        "lines": [
            "Aku coba mikir cara bilang ini berminggu-minggu.",
            "Aku suka kamu. Banget. Lebih dari yang masuk akal buat seberapa baru kita kenal.",
            "Dan aku selesai pura-pura enggak.",
            "Jadi — kita ngapain? Beneran. 🌸",
        ],
        "choices": [
            {"label": "Kita jalanin ini. Apa pun ini — aku ikut."},
            {"label": "Kayaknya kita berdua udah tau. Aku cuma mau denger kamu bilang dulu."},
            {"label": "Datang ke sini. Ayo ngomongin dengan benar."},
        ],
    },
    "CH09_END": {
        "lines": [
            "Oke. Iya. Semua itu. 🥺",
            "Aku datang.",
            "Kasih ruang di sofa itu.",
            "Dan kali ini aku gak pulang sampai beneran ada yang terjadi. 😏🌸",
            "(Bersambung — Bab 10: Punya Kamu 🌙✨)",
        ],
    },
    "CH10_N1": {
        "chapterTitle": "Punya Kamu",
        "lines": [
            "Dia datang. Dia tinggal.",
            "Pagi. Cahaya abu lembut lewat gorden. Kota masih setengah tidur.",
            "Dia meringkuk miring, rambut terurai di bantal, selimutmu penuh di sisi kasurnya. Satu bahu telanjang di atas selimut, wajahnya akhirnya tanpa jaga — tanpa performa, tanpa sadar ditatap.",
            "Cuma dia. Diam-diam, sepenuhnya di situ.",
        ],
    },
    "CH10_N2": {
        "lines": [
            "Dia bangun sebelum kamu. Bikin kopi. Kembali dan duduk di tepi kasur menatapmu dengan cara yang belum pernah.",
            "Terbuka. Yakin.",
            "Kayak yang tadinya maybe sekarang cuma iya.",
        ],
    },
    "CH10_HER1": {
        "lines": [
            "Selamat pagi 🌸",
            "Aku duduk di sini dua puluh menit mutusin ini nyata atau enggak.",
            "Terasa nyata.",
            "Bilang ini nyata.",
        ],
        "choices": [
            {"label": "Nyata. Kamu di sini. Itu bukti yang kita butuhin."},
            {"label": "Kopi yang kamu bikin nyata. Awal yang bagus."},
            {
                "label": "(Kamu raih tangannya ganti jawab.)",
                "me": "Kamu pegang tangannya.",
            },
        ],
    },
    "CH10_A": {
        "lines": [
            "Itu bukti yang kita butuhin. 🥺",
            "Oke. Iya. Aku bisa kerja dengan itu.",
            "Aku simpen kamu, BTW. Biar jelas.",
            "Kamu gak dapat suara. 🌸",
        ],
    },
    "CH10_B": {
        "lines": [
            "KOPINYA 😭",
            "Aku bikin satu cangkir dan tiba-tiba jadi bukti cinta.",
            "…Oke. Mungkin iya.",
            "Aku bikin sesuai selera kamu. Aku ingat. 🌸",
        ],
    },
    "CH10_C": {
        "lines": ["…", "Iya. Oke.", "Itu berhasil. Sempurna. 🌸"],
    },
    "CH10_MERGE": {
        "lines": [
            "Dia tinggal hampir seharian.",
            "Kamu order sarapan. Dia pinjam kaosmu. Edit foto di laptop sambil kamu baca, sesekali angkat muka bilang sesuatu yang gak ada hubungannya.",
            "Biasa aja. Persis yang bener.",
            "Sore, cahaya jadi emas, dia angkat muka dari layar.",
        ],
    },
    "CH10_END_HER": {
        "lines": [
            "Hey.",
            "Kayaknya aku lagi kena masalah.",
            "Yang bagus.",
            "Kamu bakalan susah banget buat berhenti dipikirin. Tau gak? 🌸",
        ],
    },
    "CH10_END": {
        "lines": [
            "Kamu bilang gak apa-apa bagimu.",
            "Dia senyum — yang beneran, yang gak direncanain — dan nest di sisi kamu kayak selalu ada tempat di situ.",
            "Dimulai dari like di foto tiga bulan lalu. Berakhir dengan pagi-pagi kayak ini, dan ratusan lagi menunggu.",
            "Di luar kota jalan terus seperti kota-kota, acuh dan bising.",
            "Di dalam hangat. Dan sepi. Dan miliknya. Dan milikmu.",
            "Sekarang dia sayangmu. Dan dia gak pergi ke mana-mana.",
            "— Selesai — Cerita Yui 🌸✨",
        ],
    },
}

# ---------------------------------------------------------------------------
# BRAZILIAN PORTUGUESE
# ---------------------------------------------------------------------------
PT_META = {
    "title": "Yui — Capítulo 1: A Curtida",
    "subtitle": "Ela curtiu sua foto antiga…",
}
PT = {
    "CH01_N1": {
        "chapterTitle": "A Curtida",
        "lines": [
            "A notificação apareceu enquanto você estava na cama, meio dormindo, rolando o feed.",
            "Alguém tinha curtido uma das suas fotos antigas.",
            "Não o post mais novo. Não o de ontem. Uma foto de quase três meses atrás.",
            "Curioso, você tocou na notificação.",
        ],
    },
    "CH01_N2": {
        "lines": [
            "A conta era de uma garota chamada Yui.",
            "O perfil era limpo e silenciosamente marcante — universitária, modelo freelancer de marcas de produto.",
            "Skincare. Lifestyle. De vez em quando lingerie. Não profissional, mas as marcas ficavam chamando de volta.",
            "Ela tinha um jeito que fazia tudo o que ela segurava parecer desejável.",
        ],
    },
    "CH01_SCENE": {
        "lines": [
            "Lá estava ela. Yui.",
            "Só a foto de perfil já bastava pra você parar de rolar.",
        ],
    },
    "CH01_N3": {
        "lines": [
            "A maioria ignoraria. Você não.",
            "Você abriu o perfil. Cinco minutos depois, ainda rolava.",
            "Aí percebeu — ela tinha curtido outro post seu. Mais antigo. De quase um ano.",
            "Você olhou a tela. Um sorrisinho. Decidiu mandar mensagem.",
        ],
    },
    "CH01_CHOICE": {
        "lines": ["A janela do chat abriu.", "Como você quer começar?"],
        "choices": [
            {"label": "Valeu pelas curtidas. Não esperava ninguém fuçando meu perfil assim."},
            {"label": "Acho que você bateu o recorde de foto mais antiga curtida 😏"},
            {"label": "Modelo freelancer? Isso é bem sexy, sério."},
            {
                "label": "(Curtir uma foto dela em vez de mandar mensagem.)",
                "me": "❤️ curtiu a foto dela",
            },
        ],
    },
    "CH01_A": {
        "lines": [
            "Ah! Você notou 🙈",
            "Ok, peguei — fui meio fundo. Em minha defesa, suas fotos antigas são *boas*.",
            "A maioria dos caras só posta selfie de academia. Você tem gosto.",
            "Eu sou a Yui, por sinal. Oi 🌸",
        ],
    },
    "CH01_B": {
        "lines": [
            "Hahaha ok, justo 🙊",
            "Me perdi lá. Uma foto puxou a outra e — é. Não é meu momento de orgulho.",
            "Mas não me arrependo de nada.",
            "Eu sou a Yui 🌸 legal finalmente falar oi.",
        ],
    },
    "CH01_C": {
        "lines": [
            "…Você realmente olhou a bio 😌",
            "A maioria dos caras só manda um 'oi' e torce.",
            "Faço ensaio de produto — skincare, lifestyle, um pouco de lingerie. Paga. Eu amo.",
            "Eu sou a Yui 🌸 e você acabou de me chamar atenção.",
        ],
    },
    "CH01_D": {
        "lines": [
            "Oh? 😳 Você curtiu uma minha de volta.",
            "Sem mensagem. Só… isso. Suave. Misterioso. Entendi.",
            "Agora eu *realmente* quero saber quem você é.",
            "Eu sou a Yui 🌸 sua vez.",
        ],
    },
    "CH01_MERGE": {
        "lines": [
            "O que você falou funcionou. Os pontinhos de digitando apareceram — pararam — voltaram.",
            "Como se ela estivesse escolhendo as palavras com cuidado.",
        ],
    },
    "CH01_MERGE2": {
        "lines": [
            "Ok falando sério — eu normalmente não faço isso 😅",
            "Curtir foto de estranho de um ano atrás é bem fora do meu padrão.",
            "Mas tá tarde, a cidade tá quieta, e algo em você fez eu querer falar oi de verdade.",
            "Então… você ficou feliz que eu fiz? 💕",
        ],
        "choices": [
            {"label": "Muito. Você salvou minha noite inteira."},
            {"label": "Feliz o bastante pra perdoar o ano de stalking 😏"},
            {"label": "Depende — o que te fez parar na minha foto, exatamente?"},
        ],
    },
    "CH01_END": {
        "lines": [
            "Eu devia te deixar dormir… mesmo sem querer 🌙",
            "Foi a melhor primeira conversa que eu tive em muito tempo.",
            "Me procura de novo? Vou estar esperando 🌸",
            "(Continua — Capítulo 2: Mergulho 📱)",
        ],
    },
    "CH02_N1": {
        "chapterTitle": "Mergulho",
        "lines": [
            "Manhã seguinte. Celular na mão antes de acordar de verdade.",
            "A mensagem ainda estava lá — aquela 🌸 no fim de uma linha que ela não precisava mandar.",
            "Ela tinha postado algo novo.",
        ],
    },
    "CH02_N2": {
        "lines": [
            "Ela postou uma foto nova — ensaio de produto pra uma marca de moda pequena.",
            "Uma camisola branca, alças finas e juste, o decote baixo o bastante pra mostrar a curva do peito. Ela era cheinha de um jeito que a peça não escondia — o colo pegando a luz, o busto dominando o quadro antes dos olhos chegarem em qualquer outra coisa.",
            "Mini saia no meio da coxa. Uma mão solta ao lado, queixo um pouco baixo, olhar passando da lente como se ela já soubesse o efeito e tivesse decidido deixar rolar.",
            "A legenda: *Marca nova, collab nova. A blusa e a saia são delas — a confiança é minha. 🌸*",
        ],
    },
    "CH02_POST": {
        "lines": [
            "Acabei de postar isso 🙈",
            "A marca queria algo natural e relaxado. Acho que ficou bom?",
            "Não fala sim só pra ser legal — eu percebo.",
        ],
    },
    "CH02_N3": {
        "lines": [
            "Você ficou olhando a foto mais do que pretendia.",
            "Ela parecia fácil — o tipo de fácil que exige total consciência de si.",
            "Você digitou uma resposta.",
        ],
    },
    "CH02_CHOICE": {
        "lines": ["O que você diz?"],
        "choices": [
            {"label": "Natural e relaxado? Não é a palavra. Tenta deslumbrante."},
            {"label": "A marca teve sorte. Pouca gente faz uma camisola branca ficar assim 😏"},
            {"label": "Ficou bom. Você já sabia, né."},
        ],
    },
    "CH02_A": {
        "lines": [
            "…Deslumbrante. 😳",
            "Ok eu NÃO esperava essa palavra.",
            "Fiquei uma hora olhando esse post achando que era demais e você só — ok.",
            "Você ganhou. Obrigada. Vou guardar isso. 🌸",
        ],
    },
    "CH02_B": {
        "lines": [
            "Pouca gente faz ficar assim 😏",
            "Nossa, você é PERIGO.",
            "É o elogio mais flertante que eu já recebi num ensaio de produto e eu não sei o que fazer.",
            "…Mas eu gosto. Não para. 🌸",
        ],
    },
    "CH02_C": {
        "lines": [
            "Eu já sabia. 😌",
            "Ok sim. Fine. Eu sabia.",
            "Mas é diferente quando outra pessoa fala. Especialmente alguém cuja opinião eu ligo.",
            "…Não que eu esteja dizendo que ligo. Só estou dizendo. 🌸",
        ],
    },
    "CH02_MERGE": {
        "lines": [
            "Ela puxou a conversa pro DM rápido. Uma pergunta virou dez.",
            "De tarde você sabia que ela era terceiro ano de comunicação, modelava desde os dezenove, fraca por comida apimentada e madrugada.",
            "Ela perguntou de você também — de verdade, prestando atenção em cada resposta.",
        ],
    },
    "CH02_PRIVATE": {
        "lines": [
            "Ok… já que é só a gente agora 🙈",
            "A marca só ganhou a versão safe. Essa nunca foi pro post.",
            "Eu não mando isso pra gente. Mas você não é 'gente' mais, né. 🌸",
        ],
    },
    "CH02_MERGE2": {
        "lines": [
            "Ok preciso perguntar uma coisa e você tem que ser honesto.",
            "Quando você me respondeu — foi educação, ou interesse de verdade?",
            "Porque eu tô sentindo um clima e quero saber se tô inventando 😏🌸",
        ],
        "choices": [
            {"label": "Foi interesse. Na hora. Você não tá inventando."},
            {"label": "Fiquei dez minutos no seu perfil antes de ter coragem de responder."},
            {"label": "Seu trabalho de modelo me pegou primeiro. O resto veio depois."},
        ],
    },
    "CH02_END": {
        "lines": [
            "Isso é… muito bom de ouvir 🥺",
            "Fico esperando essa conversa ficar chata e ela simplesmente não fica.",
            "Tenho ensaio amanhã. Call cedo. Mas acho que vou ficar acordada tarde mesmo assim.",
            "Não me deixa no vácuo por muito tempo, ok? 🌸",
            "(Continua — Capítulo 3: Teste de Calor 🔥)",
        ],
    },
    "CH03_N1": {
        "chapterTitle": "Teste de Calor",
        "lines": [
            "Mais três dias de mensagem. Bom dia. Áudios que ela começou a mandar em vez de digitar.",
            "A voz dela era mais quente do que você imaginava — um pouco mais grave, mais lenta, como se guardasse pro que realmente importava.",
            "No quarto dia ela mandou algo diferente.",
        ],
    },
    "CH03_N2": {
        "lines": [
            "Não era áudio. Não era foto de produto.",
            "Só ela. Cabelo solto, ombro nu onde a blusa escorregou. Olhando a câmera de frente, como um desafio.",
            "A legenda tinha três palavras: *O ensaio tava chato.*",
        ],
    },
    "CH03_N3": {
        "lines": [
            "Você olhou o celular por um tempo.",
            "Ela estava testando algo. Vocês dois sabiam.",
            "A pergunta era como você ia responder.",
        ],
    },
    "CH03_PIC": {
        "lines": [
            "Entediada entre sets então… aqui 😏",
            "Não lê demais nisso.",
            "…Ou lê. Eu não me importo. 🌸",
        ],
    },
    "CH03_CHOICE": {
        "lines": ["Como você responde?"],
        "choices": [
            {"label": "O ensaio tava chato? Isso é crime."},
            {"label": "Fiquei trinta segundos nisso e ainda não achei palavra."},
            {"label": "Ler demais? Eu já tô três capítulos fundo 😏"},
        ],
    },
    "CH03_A": {
        "lines": [
            "Crime 😂",
            "Ok mas o jeito que você falou como se o chato fosse *o ensaio* e não a foto—",
            "Você é de outro nível. Sabe disso?",
            "Eu gosto 🌸",
        ],
    },
    "CH03_B": {
        "lines": [
            "…Trinta segundos. Anotado. 😏",
            "Era a reação que eu queria.",
            "Não que eu estivesse caçando reação. Eu só tava entediada.",
            "…Ok eu tava um pouco caçando reação 🌸",
        ],
    },
    "CH03_C": {
        "lines": [
            "Três capítulos fundo 💀 me pegou.",
            "Ok você oficialmente é a pessoa mais interessante que eu falei esse mês.",
            "Talvez esse ano.",
            "Não se ache 😏🌸",
        ],
    },
    "CH03_MERGE": {
        "lines": [
            "A conversa depois tinha outra temperatura.",
            "Mais flerte. Mais de propósito. Palavras escolhidas com cuidado e mandadas mesmo assim.",
            "Ela perguntou o que você fazia no sábado como se não fosse grande coisa.",
            "Era grande coisa.",
        ],
    },
    "CH03_END": {
        "lines": [
            "Então. Sábado. Tem um café que eu amo.",
            "Eu vou quando quero sentir que a cidade é minha por um tempinho.",
            "Acho que você ia entender.",
            "Vem? 🌸",
            "(Continua — Capítulo 4: Primeiro Encontro ☕)",
        ],
    },
    "CH04_N1": {
        "chapterTitle": "Primeiro Encontro",
        "lines": [
            "Sábado. O café era exatamente como ela descreveu — quente, sem pressa, luz que fazia tudo parecer memória sendo feita.",
            "Ela já estava lá quando você entrou.",
            "Levantou o olhar do celular. Um segundo de silêncio. Depois sorriu.",
            "Pequeno. Genuíno. Como se não tivesse ensaiado.",
        ],
    },
    "CH04_N2": {
        "lines": [
            "Ela vestia algo macio e um pouco leve demais pro clima — como se tivesse escolhido de propósito.",
            "Levantou pra te cumprimentar e houve meio segundo em que ninguém sabia o movimento certo.",
            "Ela resolveu te puxando pra um abraço um compasso mais longo que o casual.",
        ],
    },
    "CH04_SCENE": {
        "lines": [
            "Ela já estava lá quando você entrou.",
            "Cabelo solto, luz macia atrás. Por um instante ela não te viu.",
            "Aquele momento pareceu importante — como ver ela antes de estar pronta pra ser vista.",
        ],
    },
    "CH04_CHOICE": {
        "lines": [
            "Você veio de verdade 🌸",
            "Eu sabia que vinha. Só falo assim quando fico nervosa.",
            "Você tá… exatamente como eu imaginei. O que é injusto.",
            "Senta. Eu peço pra você — eu sei o que você vai gostar.",
        ],
        "choices": [
            {"label": "Nervosa? Você escondeu bem."},
            {"label": "Eu também posso ser injusto. Você é mais baixa que nas fotos 😏"},
            {"label": "Você imaginou como eu seria?"},
        ],
    },
    "CH04_A": {
        "lines": [
            "Não escondi. Você só tava ocupado demais olhando em volta 😌",
            "Eu te vi entrar. Parecia confiante. Foi irritante.",
            "Ok — senta. Deixa eu me exibir um pouco. Sei esse cardápio de cor.",
        ],
    },
    "CH04_B": {
        "lines": [
            "EU TE ODEIO 😭",
            "Minhas fotos são de ângulo, obrigada.",
            "Eu sou tamanho divertido. Tem diferença.",
            "…Senta antes que eu mude de ideia sobre isso tudo 😤🌸",
        ],
    },
    "CH04_C": {
        "lines": [
            "…Não deixa estranho.",
            "Sim. Óbvio. Você tá na minha cabeça há duas semanas.",
            "Pronto. Falei. Agora senta e deixa eu me recuperar. 🌸",
        ],
    },
    "CH04_MERGE": {
        "lines": [
            "Duas horas sumiram.",
            "Ela falava com as mãos. Ria fácil. Fazia perguntas que pediam resposta de verdade e escutava todas.",
            "Em algum momento da segunda hora tirou o celular, apontou pra si e te olhou com uma sobrancelha erguida.",
        ],
    },
    "CH04_PIC": {
        "lines": [
            "Entra no frame. Quero prova que isso aconteceu 😏",
            "…Na verdade não. Deixa eu tirar uma primeiro.",
            "Pra mim. Não discute.",
        ],
    },
    "CH04_MERGE2": {
        "lines": [
            "Ok. Boa. Essa é minha.",
            "Isso foi… muito, muito bom.",
            "Não esperava gostar tanto de você ao vivo. Não é ofensa. É um problema ótimo de se ter.",
            "Quando a gente faz de novo? 🌸",
        ],
        "choices": [
            {"label": "Quando você quiser. Eu abro tempo."},
            {"label": "Fala o dia. Eu chego antes de você terminar a frase."},
            {"label": "Logo. Antes de eu começar a sentir sua falta — que já tá rolando."},
        ],
    },
    "CH04_END": {
        "lines": [
            "Essa é a resposta certa 🥺",
            "Chega bem. Me manda msg quando chegar.",
            "E não pensa demais no hoje. Só deixa ser bom.",
            "…Foi bem bom. 🌸",
            "(Continua — Capítulo 5: Por Trás da Lente 📸)",
        ],
    },
    "CH05_N1": {
        "chapterTitle": "Por Trás da Lente",
        "lines": [
            "Uma semana depois ela tinha o maior booking até agora — linha de skincare lançando em três mercados.",
            "Ficou quieta a manhã inteira. O tipo de quieto que significa nervoso.",
            "Você mandou um áudio. Quinze segundos. Só: *Você consegue. Vai ser deslumbrante.*",
            "Ela não respondeu por cinco horas.",
        ],
    },
    "CH05_N2": {
        "lines": [
            "Quando respondeu, não foi texto.",
            "Uma selfie — no meio do estúdio da marca, luzes e fundos atrás.",
            "Brilhando, um pouco orgulhosa, finalmente soltando o nervoso.",
        ],
    },
    "CH05_PIC": {
        "lines": [
            "Consegui. Essa sou eu, no estúdio de verdade da marca 😏",
            "Tive que tirar uma selfie antes de desmontarem o set.",
            "Não parava de pensar que você disse que eu seria deslumbrante. Então.",
            "Fui? 🌸",
        ],
    },
    "CH05_CHOICE": {
        "lines": ["Como você responde?"],
        "choices": [
            {"label": "Deslumbrante não cobre. Eles fizeram bem em cortar esse ângulo — é demais."},
            {"label": "Eu te falei. Guarda essa energia pro próximo."},
            {"label": "O fato de você ter me mandado *essa* especificamente… tô pensando nisso."},
        ],
    },
    "CH05_A": {
        "lines": [
            "…Demais. 😳",
            "Ok isso — preciso de um segundo.",
            "Você não pode falar essas coisas e não estar aqui.",
            "Não é justo. Sério que não é. 🌸",
        ],
    },
    "CH05_B": {
        "lines": [
            "O COFRE. 😂",
            "Ok sim. Vai pro cofre.",
            "Você é surpreendentemente bom nisso, sabia.",
            "Me fazer me sentir bem sem ficar estranho. 🌸",
        ],
    },
    "CH05_C": {
        "lines": ["…", "É.", "Eu sei o que eu fiz.", "🌸"],
    },
    "CH05_MERGE": {
        "lines": [
            "À noite ela ligou em vez de mandar msg.",
            "No telefone a voz era diferente — mais macia, sem performance.",
            "Falou do ensaio por vinte minutos e depois ficou quieta.",
            "Aí: *Fico querendo te contar as coisas primeiro. É estranho?*",
        ],
    },
    "CH05_END": {
        "lines": [
            "Não responde. Tá tudo bem. Não é estranho.",
            "É só — você facilita eu falar. Isso é raro pra mim.",
            "Não estraga sendo normal, ok? 😏🌸",
            "(Continua — Capítulo 6: Madrugada 🌙)",
        ],
    },
    "CH06_N1": {
        "chapterTitle": "Madrugada",
        "lines": [
            "01:47. Uma mensagem que você não esperava.",
            "Não pergunta. Não foto. Só:",
            "*Você tá acordado?*",
        ],
    },
    "CH06_N2": {
        "lines": [
            "Você estava. Disse que sim.",
            "Três pontinhos. Sumiram. Voltaram.",
            "Aí, de uma vez, como se tivesse decidido parar de pensar:",
        ],
    },
    "CH06_HER1": {
        "lines": [
            "Tô deitada aqui pensando em você e achei que devia te falar.",
            "Ainda não sei o que é isso. Entre a gente.",
            "Mas é alguma coisa. E eu penso nisso bastante. Mais do que planejei.",
            "…Ok. Sua vez. Fala alguma coisa. 🌸",
        ],
    },
    "CH06_CHOICE": {
        "choices": [
            {"label": "Eu penso em você o tempo todo. Desde o primeiro dia na minha cabeça."},
            {"label": "Tava deitado fazendo a mesma coisa. A gente devia falar sobre isso."},
            {"label": "Me conta no que você pensa. Específico."},
        ],
    },
    "CH06_A": {
        "lines": [
            "Desde o primeiro dia. 🥺",
            "Ok. Bom. Isso é — bem bom.",
            "Não tinha certeza se eu tava inventando.",
            "Que bom que perguntei. Quase não perguntei.",
        ],
    },
    "CH06_B": {
        "lines": [
            "A gente devia falar sobre isso.",
            "Olha você, sensato às 2 da manhã.",
            "Ok. Vamos falar.",
            "…Por onde a gente começa? 🌸",
        ],
    },
    "CH06_C": {
        "lines": [
            "ESPECÍFICO? 😳",
            "Absolutamente não. Ainda não.",
            "…Pergunta de novo daqui uma semana quando eu for mais corajosa.",
            "Ou mais tarde. Quase 2 da manhã — qualquer coisa pode rolar. 😏🌸",
        ],
    },
    "CH06_MERGE": {
        "lines": [
            "Vocês conversaram até as 3.",
            "Sobre nada específico. Sobre tudo.",
            "Em algum momento ela mandou um vídeo — deitada na cama só de sutiã e saia, cabelo pra todo lado, totalmente exposta pra você.",
            "Sem pose, sem ângulo. Só ela, sem segurar nada.",
        ],
    },
    "CH06_PIC": {
        "lines": [
            "É isso que você faz comigo — 3 da manhã, assim, só pra você 😭",
            "Nunca deixei ninguém me ver tão desfeita.",
            "…Não salva. Ok fine. Mas só porque é você. 🌸",
        ],
    },
    "CH06_END": {
        "lines": [
            "Dorme. Os dois precisam dormir.",
            "Mas fico feliz que falei.",
            "E feliz que você tava acordado.",
            "Boa noite 🌸 …Não sonha demais comigo.",
            "(Continua — Capítulo 7: Pronta 👗)",
        ],
    },
    "CH07_N1": {
        "chapterTitle": "Pronta",
        "lines": [
            "Sexta à noite. Mensagem no meio do jantar.",
            "Ela ia sair. Não com você.",
            "Aniversário de amiga. Um clube na cidade. Ela se arrumando.",
            "Mandou uma foto.",
        ],
    },
    "CH07_PIC": {
        "lines": [
            "Saindo hoje 💃",
            "Fala que eu tô bonita. Preciso do boost de confiança antes de sair. 😏🌸",
        ],
    },
    "CH07_CHOICE": {
        "lines": [
            "Ela estava incrível e sabia disso.",
            "Como você responde?",
        ],
        "choices": [
            {"label": "Você tá perigosamente bem. O povo do clube não tá pronto."},
            {"label": "Você não precisa de boost. Precisa de etiqueta de aviso."},
            {"label": "Bem? Não. Eu preciso que você não saia assim."},
        ],
    },
    "CH07_A": {
        "lines": [
            "PERIGOSAMENTE BEM 🥹",
            "Ok era exatamente o que eu precisava.",
            "Você é minha pessoa favorita, sabia?",
            "Conto tudo quando voltar. Não dorme ainda 🌸",
        ],
    },
    "CH07_B": {
        "lines": [
            "ETIQUETA DE AVISO 😭😭",
            "Ok vou printar e mostrar pra todo mundo.",
            "E depois vou pensar nisso a noite toda e vai ser bem distraído.",
            "Valeu por isso 😏🌸",
        ],
    },
    "CH07_C": {
        "lines": [
            "…",
            "Oh.",
            "OH.",
            "…Ainda vou. Mas vou pensar nisso a noite inteira. 😏🌸",
        ],
    },
    "CH07_MERGE": {
        "lines": [
            "Ela foi. Você esperou.",
            "00:43 uma msg: *Tô entediada. Todo mundo aqui é chato. Você não tá aqui. Isso é um problema.*",
            "01:15: *Voltando cedo. Não pergunta.*",
            "01:34, seu telefone tocou.",
        ],
    },
    "CH07_END": {
        "lines": [
            "Aguentei duas horas 😭",
            "O tempo todo pensando que preferia estar falando com você.",
            "É vergonhoso. Você não pode ficar convencido.",
            "…Tá convencido? 🌸",
            "(Continua — Capítulo 8: Mais Perto 🔥)",
        ],
    },
    "CH08_N1": {
        "chapterTitle": "Mais Perto",
        "lines": [
            "Duas semanas desde o café. Uma ligação de madrugada. Quarenta e poucos áudios.",
            "Ela sugeriu um segundo encontro como se não fosse importante.",
            "Era bem importante.",
            "Disse que dessa vez ia até você.",
        ],
    },
    "CH08_N2": {
        "lines": [
            "Antes de sair, mandou uma foto.",
            "Selfie no espelho. Estava arrumada — mais do que a ocasião pedia. Sabia exatamente o que fazia.",
        ],
    },
    "CH08_PIC": {
        "lines": [
            "Saio em dez. Não me deixa nervosa chegando lindo demais.",
            "Já tô nervosa o bastante 😏🌸",
        ],
    },
    "CH08_CHOICE": {
        "choices": [
            {"label": "Tarde demais. Corre."},
            {"label": "Me pedir pra não ser atraente mandando essa foto é injusto."},
            {"label": "Eu abro a porta antes de você bater."},
        ],
    },
    "CH08_A": {
        "lines": ["Tarde demais. Corre.", "…", "Já tô andando mais rápido. 🌸"],
    },
    "CH08_B": {
        "lines": [
            "Você TÁ CERTO isso é tão injusto 😭",
            "Vou apagar a foto.",
            "…Não. Você fica com ela.",
            "Ok tô saindo. 🌸",
        ],
    },
    "CH08_C": {
        "lines": [
            "A porta antes de eu bater 🥺",
            "Ok agora tô sorrindo que nem idiota na rua e o povo tá olhando.",
            "Te vejo já. 🌸",
        ],
    },
    "CH08_MERGE": {
        "lines": [
            "Ela chegou com delivery, uma briga de qual filme colocar, e zero intenção de assistir de verdade.",
            "Vocês acabaram no sofá, mais perto do que começaram.",
            "Em algum momento o filme virou barulho de fundo.",
            "Ela virou pra falar algo. Parou. Vocês estavam mais perto do que tinham percebido.",
            "O momento esticou. Quente. Carregado. Ninguém se mexeu primeiro.",
        ],
    },
    "CH08_END": {
        "lines": [
            "Eu devia ir pra casa 🌸",
            "…Eu realmente não quero.",
            "Mas se eu ficar mais um pouco algo vai acontecer e eu quero que aconteça do jeito certo.",
            "Logo. Eu falo sério. Logo.",
            "(Continua — Capítulo 9: Tudo ou Nada 💌)",
        ],
    },
    "CH09_N1": {
        "chapterTitle": "Tudo ou Nada",
        "lines": [
            "De manhã ela mandou: *Pensei na noite passada o caminho inteiro pra casa.*",
            "Você disse que também pensou.",
            "Ela sumiu por uma hora. Aí:",
        ],
    },
    "CH09_N2": {
        "lines": [
            "Chegou um vídeo.",
            "Luz do fim da tarde. O quarto dela. Fez um coraçãozinho com os dedos e te mandou um beijo voando.",
            "Foi a coisa mais vulnerável que ela te mandou.",
        ],
    },
    "CH09_PIC": {
        "lines": [
            "Fico quase falando e apagando.",
            "Então em vez disso — aqui. Um coração e um beijo. É assim que quase dizer parece.",
            "Fala alguma coisa de volta. Por favor. 🌸",
        ],
    },
    "CH09_CHOICE": {
        "choices": [
            {"label": "Eu gosto de você. Mais do que falei. Tava me segurando e não quero mais."},
            {"label": "Não vou a lugar nenhum. Quero deixar isso bem claro."},
            {"label": "Você me mandou essa foto. Acho que os dois sabem o que significa."},
        ],
    },
    "CH09_A": {
        "lines": [
            "Você tava se segurando?",
            "…Eu também.",
            "Vamos parar os dois com isso. 🌸",
        ],
    },
    "CH09_B": {
        "lines": [
            "Não vai a lugar nenhum.",
            "Meu Deus, eu precisava ouvir isso.",
            "Precisava tanto e só soube agora. 🌸",
        ],
    },
    "CH09_C": {
        "lines": ["Os dois sabem o que significa 😶", "É.", "A gente sabe. 🌸"],
    },
    "CH09_MERGE": {
        "lines": [
            "Tentei achar como dizer isso por semanas.",
            "Eu gosto de você. Muito. Mais do que faz sentido pro tempo que a gente se conhece.",
            "E cansei de fingir que não.",
            "Então — o que a gente tá fazendo? De verdade. 🌸",
        ],
        "choices": [
            {"label": "A gente tá nisso. O que for isso — eu entro."},
            {"label": "Acho que os dois já sabem. Só quero ouvir você falar primeiro."},
            {"label": "Vem pra cá. Vamos falar direito."},
        ],
    },
    "CH09_END": {
        "lines": [
            "Ok. Sim. Tudo isso. 🥺",
            "Tô indo.",
            "Abre espaço nesse sofá.",
            "E dessa vez eu não saio até algo de verdade acontecer. 😏🌸",
            "(Continua — Capítulo 10: Sua 🌙✨)",
        ],
    },
    "CH10_N1": {
        "chapterTitle": "Sua",
        "lines": [
            "Ela veio. Ela ficou.",
            "Manhã. Luz cinza macia nas cortinas. A cidade ainda meio dormindo.",
            "Ela encolhida de lado, cabelo solto no travesseiro, seu cobertor inteiro do lado dela da cama. Um ombro nu acima do lençol, o rosto finalmente sem guarda — sem performance, sem saber que olhavam.",
            "Só ela. Quietamente, completamente ali.",
        ],
    },
    "CH10_N2": {
        "lines": [
            "Acordou antes de você. Fez café. Voltou e sentou na beira da cama te olhando de um jeito que nunca tinha te olhado.",
            "Aberta. Decidida.",
            "Como se o talvez agora fosse só sim.",
        ],
    },
    "CH10_HER1": {
        "lines": [
            "Bom dia 🌸",
            "Fiquei vinte minutos aqui decidindo se isso é real.",
            "Parece real.",
            "Me diz que é real.",
        ],
        "choices": [
            {"label": "É real. Você tá aqui. É toda a prova que a gente precisa."},
            {"label": "O café que você fez é real. Bom começo."},
            {
                "label": "(Você pega a mão dela em vez de responder.)",
                "me": "Você pega a mão dela.",
            },
        ],
    },
    "CH10_A": {
        "lines": [
            "É toda a prova que a gente precisa. 🥺",
            "Ok. Sim. Eu trabalho com isso.",
            "Vou te ficar, por sinal. Só pra deixar claro.",
            "Você não tem voto. 🌸",
        ],
    },
    "CH10_B": {
        "lines": [
            "O CAFÉ 😭",
            "Faço uma xícara e de repente é prova de amor.",
            "…Ok. Talvez seja.",
            "Fiz do jeito que você toma. Eu lembrei. 🌸",
        ],
    },
    "CH10_C": {
        "lines": ["…", "É. Ok.", "Funciona. Funciona perfeitamente. 🌸"],
    },
    "CH10_MERGE": {
        "lines": [
            "Ela ficou a maior parte do dia.",
            "Vocês pediram café da manhã. Ela pegou uma camisa sua emprestada. Editava fotos no notebook enquanto você lia, às vezes levantando o olhar pra falar algo que não tinha a ver com nada.",
            "Era comum. Era exatamente certo.",
            "No fim da tarde, com a luz dourando, ela levantou o olhar da tela.",
        ],
    },
    "CH10_END_HER": {
        "lines": [
            "Ei.",
            "Acho que eu tô encrencada.",
            "Do tipo bom.",
            "Você vai ser bem difícil de parar de pensar. Sabia? 🌸",
        ],
    },
    "CH10_END": {
        "lines": [
            "Você disse que por você tudo bem.",
            "Ela sorriu — o de verdade, o sem ensaio — e se acomodou no seu lado como se sempre tivesse tido um lugar ali.",
            "Começou com uma curtida numa foto de três meses atrás. Terminou com manhãs como essa, e centenas mais esperando.",
            "Lá fora a cidade segue como cidades fazem, indiferente e barulhenta.",
            "Lá dentro é quente. E quieto. E dela. E seu.",
            "Ela é sua querida agora. E não vai a lugar nenhum.",
            "— Fim — A história da Yui 🌸✨",
        ],
    },
}

def write_locale(code: str, meta: dict, nodes_t: dict, en: dict) -> Path:
    out = apply(en, meta, nodes_t)
    path = OUT_DIR / f"{code}.json"
    path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def main() -> int:
    en = json.loads(EN_PATH.read_text(encoding="utf-8"))
    # RU / HI live in sibling module to keep this file manageable
    from yui_i18n_ru_hi import HI, HI_META, RU, RU_META  # type: ignore

    for code, meta, table in (
        ("id", ID_META, ID),
        ("pt", PT_META, PT),
        ("ru", RU_META, RU),
        ("hi", HI_META, HI),
    ):
        path = write_locale(code, meta, table, en)
        print(f"wrote {path.relative_to(ROOT)} ({len(table)} nodes)")
    return 0


if __name__ == "__main__":
    # allow importing sibling from tools/
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    raise SystemExit(main())
