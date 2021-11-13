<h1 align="center"><b>Ini adalah simpel multiple tools untuk Facebook</b></h1>

<div align="center">
  <a href="https://github.com/lumine-id">
    <img alt="Python 3.5^" src="https://img.shields.io/badge/Python-3.5^-success.svg"/>
  </a>
  <a href="https://github.com/lumine-id">
    <img alt="Last Commit" src="https://img.shields.io/github/last-commit/lumine-id/lumine.svg"/>
  </a>
   <a href="https://github.com/lumine-id">
    <img alt="Repo Size" src="https://img.shields.io/github/repo-size/lumine-id/lumine.svg"/>
  </a>
  <a href="https://github.com/lumine-id">
    <img alt="Starts" src="https://img.shields.io/github/stars/lumine-id/lumine.svg"/>
  </a>
  <a href="https://github.com/lumine-id">
    <img alt="Forks" src="https://img.shields.io/github/forks/lumine-id/lumine.svg"/>
  </a>
</div>
<br>

Jika kamu menggunakan Termux Android silahkan download Termux dari link dibawah ini jangan dari PlayStore.

Link download Termux: [https://f-droid.org/repo/com.termux_117.apk](https://f-droid.org/repo/com.termux_117.apk)

## Install paket dan clone repository
```sh
pkg update && pkg upgrade
pkg install python git clang
python -m pip install --upgrade pip
git clone https://github.com/lumine-id/lumine
```

## Masuk ke folder
```sh
cd lumine
```

## Setup
Jika kamu baru pertama install script silahkan jalankan perintah dibawah ini
```sh
python -m pip install -r requirements.txt
python setup.py build_ext --inplace -j 5
```
Tunggu sampe proses compile selesai, mungkin memerlukan waktu sedikit lama.

## Akhirnya
Sekarang tinggal jalanin perintah ini untuk menjalankan script
```sh
./lumine
```
Dan selamat menggunakan 🤗

## Disclaimer
Kami tidak bertanggung jawab atas penyalahgunaan alat ini
Atas apapun yang anda lakukan adalah tanggung jawab masing-masing

## Ada pertanyaan?
Kebingungan cara install script nya atau mungkin mengalami masalah? 🤔
silahkan boleh tanya-tanya tapi dilarang nanya soal masalah akun facebook, Terimakasih.
