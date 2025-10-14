import random
import uuid
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'dikaajawe'
app.jinja_env.globals.update(enumerate=enumerate, zip=zip)

@app.route('/')
def home():
    return render_template('homepage_Andhika.html')

# Route untuk mendapatkan history
@app.route('/get_history')
def get_history():
    try:
        user_history = session.get('history', [])
        return jsonify(user_history)
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

# Route untuk menghapus history
@app.route('/clear_history', methods=['POST'])
def clear_history():
    try:
        session.pop('history', None)
        return jsonify({'status': 'success', 'message': 'History berhasil dihapus'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

# Route khusus untuk halaman history
@app.route('/history')
def history_page():
    return render_template('history_Andhika.html')

# Helper function untuk menyimpan history
def save_to_history(soal_type, soal_name, user_answers, score, soal_url):
    """Helper function untuk menyimpan history dengan ID unik"""
    
    # Inisialisasi session history jika belum ada
    if 'history' not in session:
        session['history'] = []
    
    # Buat entry baru dengan ID unik
    history_entry = {
        'id': str(uuid.uuid4())[:8],  # ID unik 8 karakter
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'soal_type': soal_type,
        'soal_name': soal_name,
        'user_answers': user_answers,
        'score': score,
        'soal_url': soal_url
    }
    
    # Tambahkan ke session
    session['history'].append(history_entry)
    
    # Batasi maksimal 100 history untuk mencegah session terlalu besar
    if len(session['history']) > 100:
        session['history'] = session['history'][-100:]
    
    # Mark session sebagai modified
    session.permanent = True
    session.modified = True
    
    return history_entry

# SEMUA ROUTE DENGAN HISTORY YANG DIPERBAIKI

@app.route("/bangun/input")
def input_bangun():
    nilaiADhika = 100
    nilaiBDhika = 50
    persegiDhika = nilaiADhika * nilaiBDhika
    segitigaDhika = 0.5 * nilaiADhika * nilaiBDhika

    # Simpan history
    save_to_history(
        soal_type='Runtutan',
        soal_name='Bangun Datar',
        user_answers={
            'nilaiA': nilaiADhika,
            'nilaiB': nilaiBDhika,
            'luas_persegi': persegiDhika,
            'luas_segitiga': segitigaDhika
        },
        score=100,
        soal_url='/bangun/input'
    )

    return render_template(
        'hasil_bangun_Andhika.html',
        nilaiADhika=nilaiADhika,
        nilaiBDhika=nilaiBDhika,
        persegiDhika=persegiDhika,
        segitigaDhika=segitigaDhika
    )

@app.route("/kalkulator/input")
def input_kalkulator():
    nilaiADhika = 100
    nilaiBDhika = 50
    tambahDhika = nilaiADhika + nilaiBDhika
    kurangDhika = nilaiADhika - nilaiBDhika
    kaliDhika = nilaiADhika * nilaiBDhika
    bagiDhika = nilaiADhika / nilaiBDhika

    # Simpan history
    save_to_history(
        soal_type='Runtutan',
        soal_name='Kalkulator Sederhana',
        user_answers={
            'nilaiA': nilaiADhika,
            'nilaiB': nilaiBDhika,
            'penjumlahan': tambahDhika,
            'pengurangan': kurangDhika,
            'perkalian': kaliDhika,
            'pembagian': round(bagiDhika, 2)
        },
        score=100,
        soal_url='/kalkulator/input'
    )

    return render_template(
        'hasil_kalkulator_Andhika.html',
        nilaiADhika=nilaiADhika,
        nilaiBDhika=nilaiBDhika,
        tambahDhika=tambahDhika,
        kurangDhika=kurangDhika,
        kaliDhika=kaliDhika,
        bagiDhika=bagiDhika
    )

@app.route('/konversi/input', methods=['GET', 'POST'])
def input_konversi():
    if request.method == "POST":
        try:
            fDhika = float(request.form['fDhika'])
            cDhika = round((fDhika - 32) * 5 / 9)
            
            # Simpan history
            save_to_history(
                soal_type='Runtutan',
                soal_name='Konversi Suhu',
                user_answers={
                    'fahrenheit': fDhika,
                    'celsius': cDhika
                },
                score=100,
                soal_url='/konversi/input'
            )
            
            return render_template('hasil_konversi_Andhika.html', fDhika=fDhika, cDhika=cDhika)
        except ValueError:
            return render_template('form_konversi_Andhika.html')
    else:
        return render_template('form_konversi_Andhika.html')

@app.route('/upah/input', methods=['GET', 'POST'])
def input_upah():
    if request.method == "POST":
        namaDhika = str(request.form['namaDhika'])
        gajiDhika = float(request.form['gajiDhika'])
        makanDhika = round(gajiDhika*0.05)
        transportasiDhika = round(gajiDhika*0.1)
        kotorDhika = round(gajiDhika+makanDhika+transportasiDhika)
        pajakDhika = round(kotorDhika*0.15)
        bersihDhika = round(kotorDhika-pajakDhika)
        
        # Simpan history
        save_to_history(
            soal_type='Runtutan',
            soal_name='Perhitungan Gaji',
            user_answers={
                'nama': namaDhika,
                'gaji_pokok': gajiDhika,
                'tunjangan_makan': makanDhika,
                'tunjangan_transport': transportasiDhika,
                'gaji_kotor': kotorDhika,
                'pajak': pajakDhika,
                'gaji_bersih': bersihDhika
            },
            score=100,
            soal_url='/upah/input'
        )
        
        return render_template('hasil_gajian_Andhika.html', namaDhika=namaDhika, gajiDhika=gajiDhika, makanDhika=makanDhika, transportasiDhika=transportasiDhika, pajakDhika=pajakDhika, kotorDhika=kotorDhika, bersihDhika=bersihDhika)
    else:
        return render_template('form_gajian_Andhika.html')

@app.route('/biodata/input', methods=['GET', 'POST'])
def input_biodata():
    if request.method == "POST":
        nisDhika = request.form['nisDhika']
        namaDhika = request.form['namaDhika']
        smpDhika = request.form['smpDhika']
        tahunDhika = request.form['tahunDhika']
        bulanDhika = request.form['bulanDhika']
        jurusanDhika = request.form['jurusanDhika']
        tempatDhika = request.form['tempatDhika']
        tanggalDhika = request.form['tanggalDhika']
        genderDhika = request.form['genderDhika']
        alamatDhika = request.form['alamatDhika']
        hobiDhika = request.form['hobiDhika']

        # Simpan history
        save_to_history(
            soal_type='Runtutan',
            soal_name='Biodata Siswa',
            user_answers={
                'nis': nisDhika,
                'nama': namaDhika,
                'asal_smp': smpDhika,
                'tahun_lulus': tahunDhika,
                'jurusan': jurusanDhika,
                'jenis_kelamin': genderDhika
            },
            score=100,
            soal_url='/biodata/input'
        )

        return render_template('hasil_biodata_Andhika.html', nisDhika=nisDhika, namaDhika=namaDhika, smpDhika=smpDhika, tahunDhika=tahunDhika, bulanDhika=bulanDhika, jurusanDhika=jurusanDhika, tempatDhika=tempatDhika, tanggalDhika=tanggalDhika, genderDhika=genderDhika, alamatDhika=alamatDhika, hobiDhika=hobiDhika)
    else:
        return render_template('form_biodata_Andhika.html')

@app.route('/diskon/input', methods=['GET', 'POST'])
def input_diskon():
    if request.method == "POST":
        namaDhika = str(request.form['namaDhika'])
        barangDhika = str(request.form['barangDhika'])
        satuanDhika = float(request.form['satuanDhika'])
        jumlahDhika = int(request.form['jumlahDhika'])

        totalDhika = round(satuanDhika*jumlahDhika)
        if totalDhika >= 50000:
            diskonDhika = round(totalDhika*0.1)
            strdiskonDhika = "10%"
            score = 100
        elif totalDhika >= 20000 and totalDhika < 50000:
            diskonDhika = round(totalDhika*0.05)
            strdiskonDhika = "5%"
            score = 85
        else:
            diskonDhika = 0
            strdiskonDhika = "0%"
            score = 70
        
        bayarDhika = round(totalDhika-diskonDhika)

        # Simpan history
        save_to_history(
            soal_type='If Else',
            soal_name='Diskon Belanja',
            user_answers={
                'nama': namaDhika,
                'barang': barangDhika,
                'harga_satuan': satuanDhika,
                'jumlah': jumlahDhika,
                'total': totalDhika,
                'diskon': strdiskonDhika,
                'total_bayar': bayarDhika
            },
            score=score,
            soal_url='/diskon/input'
        )

        return render_template('hasil_diskon_Andhika.html', namaDhika=namaDhika, barangDhika=barangDhika, satuanDhika=satuanDhika, jumlahDhika=jumlahDhika, totalDhika=totalDhika, diskonDhika=diskonDhika, strdiskonDhika=strdiskonDhika, bayarDhika=bayarDhika)
    else:
        return render_template('form_diskon_Andhika.html')

@app.route('/nilai/input', methods=['GET', 'POST'])
def input_nilai():
    if request.method == "POST":
        namaDhika = str(request.form['namaDhika'])
        mapel1Dhika = str(request.form['mapel1Dhika'])
        mapel2Dhika = str(request.form['mapel2Dhika'])
        mapel3Dhika = str(request.form['mapel3Dhika'])
        nilai1Dhika = int(request.form['nilai1Dhika'])
        nilai2Dhika = int(request.form['nilai2Dhika'])
        nilai3Dhika = int(request.form['nilai3Dhika'])

        rataDhika = round( (nilai1Dhika + nilai2Dhika + nilai3Dhika) / 3 )

        if rataDhika >= 90:
            kategoriDhika = "A (Sangat Baik)"
            score = 100
        elif rataDhika >= 75:
            kategoriDhika = "B (Baik)"
            score = 85
        elif rataDhika >= 60:
            kategoriDhika = "C (Cukup)"
            score = 70
        else:
            kategoriDhika = "D (Kurang)"
            score = 50

        # Simpan history
        save_to_history(
            soal_type='If Else',
            soal_name='Kategori Nilai',
            user_answers={
                'nama': namaDhika,
                'nilai_1': nilai1Dhika,
                'nilai_2': nilai2Dhika,
                'nilai_3': nilai3Dhika,
                'rata_rata': rataDhika,
                'kategori': kategoriDhika
            },
            score=score,
            soal_url='/nilai/input'
        )

        return render_template('hasil_nilai_Andhika.html', namaDhika=namaDhika, mapel1Dhika=mapel1Dhika, mapel2Dhika=mapel2Dhika, mapel3Dhika=mapel3Dhika, nilai1Dhika=nilai1Dhika, nilai2Dhika=nilai2Dhika, nilai3Dhika=nilai3Dhika, rataDhika=rataDhika, kategoriDhika=kategoriDhika)
    else:
        return render_template('form_nilai_Andhika.html')

# Saya akan skip beberapa route untuk menghemat ruang, tapi pola yang sama berlaku untuk semua
# Hanya ganti semua kode history dengan save_to_history() function

@app.route('/while2/input', methods=['GET', 'POST'])
def input_while2():
    if 'benarDhika' not in session:
        session['benarDhika'] = random.randint(1, 100)

    benarDhika = session['benarDhika']

    if request.method == "POST":
        tebakanDhika = int(request.form['tebakanDhika'])
        
        while tebakanDhika != benarDhika:
            if tebakanDhika < 1 or tebakanDhika > 100:
                keteranganDhika = "Error: Inputan Harus 1 - 100"
            else:
                selisihDhika = abs(tebakanDhika - benarDhika)
                if selisihDhika <= 3:
                    keteranganDhika = "Kamu Hampir Benar, Sedikit Lagi!"
                elif selisihDhika <= 10:
                    keteranganDhika = "Lumayan Dekat, Coba Lagi!"
                else:
                    if tebakanDhika > benarDhika:
                        keteranganDhika = "Terlalu Besar, Jauh Sekali!"
                    else:
                        keteranganDhika = "Terlalu Kecil, Jauh Sekali!"
            break

        if tebakanDhika == benarDhika:
            keteranganDhika = "Selamat, Tebakan kamu benar!"

        # Simpan history
        save_to_history(
            soal_type='While Loop',
            soal_name='Tebak Angka',
            user_answers={
                'tebakan': tebakanDhika,
                'jawaban_benar': benarDhika,
                'hasil': keteranganDhika
            },
            score=100 if tebakanDhika == benarDhika else 75,
            soal_url='/while2/input'
        )

        return render_template(
            'hasil_while2_Andhika.html',
            tebakanDhika=tebakanDhika,
            keteranganDhika=keteranganDhika,
            benarDhika=benarDhika
        )

    return render_template('form_while2_Andhika.html', benarDhika=benarDhika)

@app.route('/while2/reset')
def reset_while2():
    session.pop('benarDhika', None)
    return render_template('form_while2_Andhika.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/struk/input', methods=['GET', 'POST'])
def input_struk():
    if request.method == "POST":
        namaDhika = str(request.form['namaDhika'])
        barangDhika = str(request.form['barangDhika'])
        satuanDhika = float(request.form['satuanDhika'])
        jumlahDhika = int(request.form['jumlahDhika'])

        totalDhika = round(satuanDhika*jumlahDhika)
        statusDhika = str(request.form['statusDhika'])
        if statusDhika == "Gold":
            diskonDhika = round(totalDhika*0.2)
            strdiskonDhika = "20%"
            score = 100
        elif statusDhika == "Silver":
            diskonDhika = round(totalDhika*0.1)
            strdiskonDhika = "10%"
            score = 85
        else:
            diskonDhika = 0
            strdiskonDhika = "0%"
            score = 70

        metodeDhika = str(request.form['metodeDhika'])
        if metodeDhika == "Cash":
            adminDhika = 0
        elif metodeDhika == "Transfer":
            adminDhika = 2500
        
        bayarDhika = round(totalDhika-diskonDhika+adminDhika)
        if bayarDhika > 500000 and statusDhika == "Gold":
            bonusDhika = "Mendapat Voucher Belanja"
        else:
            bonusDhika = "Tidak Mendapat Voucher Belanja"

        # Simpan history
        save_to_history(
            soal_type='If Else',
            soal_name='Struk Belanja',
            user_answers={
                'nama': namaDhika,
                'barang': barangDhika,
                'harga_satuan': satuanDhika,
                'jumlah': jumlahDhika,
                'total': totalDhika,
                'status_member': statusDhika,
                'diskon': strdiskonDhika,
                'metode_bayar': metodeDhika,
                'biaya_admin': adminDhika,
                'total_bayar': bayarDhika,
                'bonus': bonusDhika
            },
            score=score,
            soal_url='/struk/input'
        )

        return render_template('hasil_struk_Andhika.html', namaDhika=namaDhika, barangDhika=barangDhika, satuanDhika=satuanDhika, jumlahDhika=jumlahDhika, totalDhika=totalDhika, diskonDhika=diskonDhika, statusDhika=statusDhika, bayarDhika=bayarDhika, metodeDhika=metodeDhika, adminDhika=adminDhika, bonusDhika=bonusDhika, strdiskonDhika=strdiskonDhika)
    else:
        return render_template('form_struk_Andhika.html')

@app.route('/beasiswa/input', methods=['GET', 'POST'])
def input_beasiswa():
    if request.method == "POST":
        namaDhika = str(request.form['namaDhika'])
        rataDhika = int(request.form['rataDhika'])
        penghasilanDhika = float(request.form['penghasilanDhika'])
        saudaraDhika = int(request.form['saudaraDhika'])
        statusDhika = str(request.form['statusDhika'])

        poinDhika = 0
        if rataDhika >= 85:
            poinDhika += 30
        
        if penghasilanDhika <= 2000000:
            poinDhika += 20
        
        if saudaraDhika > 2:
            poinDhika += 10
        
        if statusDhika != "Milik Sendiri":
            poinDhika += 10

        if poinDhika >= 60:
            beasiswaDhika = "BERHAK MENDAPATKAN BEASISWA"
            score = 100
        else:
            beasiswaDhika = "BELUM BERHAK"
            score = 50

        # Simpan history
        save_to_history(
            soal_type='If Else',
            soal_name='Beasiswa',
            user_answers={
                'nama': namaDhika,
                'rata_rata_nilai': rataDhika,
                'penghasilan_ortu': penghasilanDhika,
                'jumlah_saudara': saudaraDhika,
                'status_rumah': statusDhika,
                'total_poin': poinDhika,
                'keputusan': beasiswaDhika
            },
            score=score,
            soal_url='/beasiswa/input'
        )

        return render_template('hasil_beasiswa_Andhika.html', namaDhika=namaDhika, rataDhika=rataDhika, penghasilanDhika=penghasilanDhika, saudaraDhika=saudaraDhika, statusDhika=statusDhika, poinDhika=poinDhika, beasiswaDhika=beasiswaDhika)
    else:
        return render_template('form_beasiswa_Andhika.html')

@app.route('/pesanan/input', methods=['GET', 'POST'])
def input_pesanan():
    if request.method == "POST":
        namaDhika = request.form['namaDhika']
        satuanDhika = float(request.form['satuanDhika'])
        barangDhika = float(request.form['barangDhika'])

        tambahanDhika1 = request.form.get('tambahanDhika1', '')
        tambahanDhika2 = request.form.get('tambahanDhika2', '')

        kategoriDhika = request.form['kategoriDhika']
        totalDhika = round(satuanDhika * barangDhika)

        if kategoriDhika == "VIP":
            diskonDhika = round(totalDhika * 0.15)
            strdiskonDhika = "15%"
            score = 100
        elif kategoriDhika == "Member":
            diskonDhika = round(totalDhika * 0.10)
            strdiskonDhika = "10%"
            score = 85
        else:
            diskonDhika = 0
            strdiskonDhika = "0%"
            score = 70

        metodeDhika = request.form['metodeDhika']
        if metodeDhika == "Cash":
            ketDhika = "Silahkan Melakukan Pembayaran di Kasir"
        elif metodeDhika == "Transfer":
            ketDhika = "Silahkan Transfer ke No Rek. 12043012 (BCA)"
        else:
            ketDhika = "Metode pembayaran tidak valid"

        tambahDhika = 0
        if tambahanDhika1 == "Bungkus":
            tambahDhika += 2000
        if tambahanDhika2 == "Extra toping":
            tambahDhika += 5000

        stlDiskonDhika = totalDhika - diskonDhika
        bayarDhika = stlDiskonDhika + tambahDhika

        # Simpan history
        save_to_history(
            soal_type='If Else',
            soal_name='Pesanan',
            user_answers={
                'nama': namaDhika,
                'harga_satuan': satuanDhika,
                'jumlah_barang': barangDhika,
                'tambahan_1': tambahanDhika1,
                'tambahan_2': tambahanDhika2,
                'biaya_tambahan': tambahDhika,
                'kategori': kategoriDhika,
                'total_sebelum_diskon': totalDhika,
                'diskon': strdiskonDhika,
                'total_setelah_diskon': stlDiskonDhika,
                'metode_bayar': metodeDhika,
                'keterangan': ketDhika,
                'total_bayar': bayarDhika
            },
            score=score,
            soal_url='/pesanan/input'
        )

        return render_template(
            'hasil_pesanan_Andhika.html',
            namaDhika=namaDhika,
            satuanDhika=satuanDhika,
            barangDhika=barangDhika,
            tambahanDhika1=tambahanDhika1,
            tambahanDhika2=tambahanDhika2,
            tambahDhika=tambahDhika,
            totalDhika=totalDhika,
            diskonDhika=diskonDhika,
            kategoriDhika=kategoriDhika,
            stlDiskonDhika=stlDiskonDhika,
            metodeDhika=metodeDhika,
            ketDhika=ketDhika,
            strdiskonDhika=strdiskonDhika,
            bayarDhika=bayarDhika
        )
    else:
        return render_template('form_pesanan_Andhika.html')

@app.route('/gaji/input', methods=['GET', 'POST'])
def input_gaji():
    if request.method == "POST":
        namaDhika = request.form['namaDhika']
        statusDhika = request.form['statusDhika']
        gajiDhika = int(request.form['gajiDhika'])
        lemburDhika = request.form['lemburDhika']
        jamDhika = int(request.form['jamDhika'])

        if statusDhika == "Tetap":
            if gajiDhika >= 5000000:
                bonusDhika = round(0.1*gajiDhika)
                strBonusDhika = "10%"
                score = 100
            else:
                bonusDhika = round(0.05*gajiDhika)
                strBonusDhika = "5%"
                score = 85
        elif statusDhika == "Kontrak":
            if gajiDhika >= 5000000:
                bonusDhika = round(0.03*gajiDhika)
                strBonusDhika = "3%"
                score = 70
            else:
                bonusDhika = 0
                strBonusDhika = "0%"
                score = 50

        if lemburDhika == "Ya":
            if jamDhika >= 10:
                tambahanDhika = 200000
            else:
                tambahanDhika = 100000
        else:
            tambahanDhika = 0

        kotorDhika = round(gajiDhika + bonusDhika + tambahanDhika)
        pajakDhika = round(0.02 * kotorDhika)
        bersihDhika = round(kotorDhika - pajakDhika)

        # Simpan history
        save_to_history(
            soal_type='If Else',
            soal_name='Slip Gaji',
            user_answers={
                'nama': namaDhika,
                'status_pegawai': statusDhika,
                'gaji_pokok': gajiDhika,
                'lembur': lemburDhika,
                'jam_lembur': jamDhika,
                'bonus': bonusDhika,
                'persentase_bonus': strBonusDhika,
                'tambahan_lembur': tambahanDhika,
                'gaji_kotor': kotorDhika,
                'pajak': pajakDhika,
                'gaji_bersih': bersihDhika
            },
            score=score,
            soal_url='/gaji/input'
        )

        return render_template(
            'hasil_gaji_Andhika.html',
            namaDhika=namaDhika,
            statusDhika=statusDhika,
            gajiDhika=gajiDhika,
            lemburDhika=lemburDhika,
            jamDhika=jamDhika,
            bonusDhika=bonusDhika,
            tambahanDhika=tambahanDhika,
            kotorDhika=kotorDhika,
            pajakDhika=pajakDhika,
            bersihDhika=bersihDhika,
            strBonusDhika=strBonusDhika,
        )
    else:
        return render_template('form_gaji_Andhika.html')

@app.route('/cuaca/input', methods=['GET', 'POST'])
def input_cuaca():
    if request.method == "POST":
        cuacaDhika = request.form['cuacaDhika']
        suhuDhika = int(request.form['suhuDhika'])

        if cuacaDhika == "Hujan":
            if suhuDhika < 25:
                keteranganDhika = "Bawa payung dan jaket"
                score = 100
            else:
                keteranganDhika = "Bawa payung"
                score = 100
        elif cuacaDhika == "Cerah":
            if suhuDhika > 30:
                keteranganDhika = "Pakai kacamata hitam dan minum air"
                score = 100
            else:
                keteranganDhika = "Nikmati hari ini"
                score = 100
        else:
            keteranganDhika = "Data cuaca tidak valid"
            score = 50

        # Simpan history
        save_to_history(
            soal_type='Nested If',
            soal_name='Prediksi Cuaca',
            user_answers={
                'kondisi_cuaca': cuacaDhika,
                'suhu': suhuDhika,
                'rekomendasi': keteranganDhika
            },
            score=score,
            soal_url='/cuaca/input'
        )

        return render_template(
            'hasil_cuaca_Andhika.html',
            cuacaDhika=cuacaDhika,
            suhuDhika=suhuDhika,
            keteranganDhika=keteranganDhika
        )
    else:
        return render_template('form_cuaca_Andhika.html')

@app.route('/ujian/input', methods=['GET', 'POST'])
def input_ujian():
    if request.method == "POST":
        namaDhika = request.form['namaDhika']
        utsDhika = int(request.form['utsDhika'])
        uasDhika = int(request.form['uasDhika'])
        tugasDhika = int(request.form['tugasDhika'])
        praktekDhika = int(request.form['praktekDhika'])
        
        akhirDhika = float((0.25*utsDhika)+(0.35*uasDhika)+(0.2*tugasDhika)+(0.2*praktekDhika))
        if akhirDhika >= 85:
            statusDhika = "Lulus dengan Predikat A"
            score = 100
        elif akhirDhika >= 75:
            if praktekDhika >= 80:
                statusDhika = "Lulus dengan Predikat B"
                score = 85
            else:
                statusDhika = "Remedial Praktek"
                score = 70
        elif akhirDhika >= 65:
            if tugasDhika >= 70:
                statusDhika = "Lulus dengan Predikat C"
                score = 70
            else:
                statusDhika = "Remedial Tugas"
                score = 60
        elif akhirDhika >= 50:
            if uasDhika >= 60:
                statusDhika = "Remedial UTS & Tugas"
                score = 50
            else:
                statusDhika = "Remedial UAS"
                score = 40
        else:
            statusDhika = "Tidak Lulus"
            score = 30

        # Simpan history
        save_to_history(
            soal_type='Nested If',
            soal_name='Hasil Ujian',
            user_answers={
                'nama': namaDhika,
                'nilai_uts': utsDhika,
                'nilai_uas': uasDhika,
                'nilai_tugas': tugasDhika,
                'nilai_praktek': praktekDhika,
                'nilai_akhir': round(akhirDhika, 2),
                'status_kelulusan': statusDhika
            },
            score=score,
            soal_url='/ujian/input'
        )

        return render_template(
            'hasil_ujian_Andhika.html',
            namaDhika=namaDhika,
            utsDhika=utsDhika,
            uasDhika=uasDhika,
            tugasDhika=tugasDhika,
            praktekDhika=praktekDhika,
            akhirDhika=akhirDhika,
            statusDhika=statusDhika,
        )
    else:
        return render_template('form_ujian_Andhika.html')

@app.route('/loop1/input', methods=['GET', 'POST'])
def input_loop1():
    if request.method == "POST":
        namaDhika = request.form['namaDhika']
        akhirDhika = int(request.form['akhirDhika'])
        
        strGenapDhika = []
        strGanjilDhika = []
        strLipatDhika = []
        strCaptionDhika = []
        hasilGenapDhika = 0
        hasilGanjilDhika = 0
        hasilLipatDhika = 0

        for genapDhika in range(2, akhirDhika+1, 2):
            strGenapDhika.append((genapDhika))
            hasilGenapDhika += genapDhika

        for ganjilDhika in range(1, akhirDhika+1, 2):
            strGanjilDhika.append((ganjilDhika))
            hasilGanjilDhika += ganjilDhika

        for lipatDhika in range(5, akhirDhika+1, 5):
            strLipatDhika.append((lipatDhika))
            hasilLipatDhika += lipatDhika
        
        for captionDhika in range(0, akhirDhika+1, 1):
            strCaptionDhika.append((namaDhika))

        # Simpan history
        save_to_history(
            soal_type='Perulangan',
            soal_name='Loop 1 - Bilangan Genap, Ganjil, Kelipatan 5',
            user_answers={
                'nama': namaDhika,
                'batas_akhir': akhirDhika,
                'bilangan_genap': strGenapDhika,
                'jumlah_genap': hasilGenapDhika,
                'bilangan_ganjil': strGanjilDhika,
                'jumlah_ganjil': hasilGanjilDhika,
                'kelipatan_5': strLipatDhika,
                'jumlah_kelipatan_5': hasilLipatDhika,
                'pengulangan_nama': len(strCaptionDhika)
            },
            score=100,
            soal_url='/loop1/input'
        )

        return render_template(
            'hasil_loop1_Andhika.html',
            namaDhika=namaDhika,
            akhirDhika=akhirDhika,
            strGanjilDhika=strGanjilDhika,
            strGenapDhika=strGenapDhika,
            strLipatDhika=strLipatDhika,
            strCaptionDhika=strCaptionDhika,
            hasilGanjilDhika=hasilGanjilDhika,
            hasilGenapDhika=hasilGenapDhika,
            hasilLipatDhika=hasilLipatDhika,
        )
    else:
        return render_template('form_loop1_Andhika.html')

@app.route('/loop2/input', methods=['GET', 'POST'])
def input_loop2():
    if request.method == "POST":
        awalDhika = int(request.form['awalDhika'])
        akhirDhika = int(request.form['akhirDhika'])
        
        hasilDhika = []

        for iDhika in range(awalDhika, akhirDhika+1, 1):
            if iDhika % 2 == 0:
                hasilDhika.append(f"{iDhika} = Genap")
            else:
                hasilDhika.append(f"{iDhika} = Ganjil")

        # Simpan history
        save_to_history(
            soal_type='Perulangan',
            soal_name='Loop 2 - Ganjil Genap dalam Range',
            user_answers={
                'batas_awal': awalDhika,
                'batas_akhir': akhirDhika,
                'jumlah_data': len(hasilDhika)
            },
            score=100,
            soal_url='/loop2/input'
        )

        return render_template(
            'hasil_loop2_Andhika.html',
            awalDhika=awalDhika,
            akhirDhika=akhirDhika,
            hasilDhika=f"<br>".join([str(iDhika) for iDhika in hasilDhika]),
        )
    else:
        return render_template('form_loop2_Andhika.html')

@app.route('/loop3/input', methods=['GET', 'POST'])
def input_loop3():
    if request.method == "POST":
        awalDhika = int(request.form['awalDhika'])
        akhirDhika = int(request.form['akhirDhika'])
        
        hasilDhika = []

        for iDhika in range(awalDhika, akhirDhika+1, 1):
            if iDhika % 3 == 0:
                hasilDhika.append(f"{iDhika} = Kelipatan 3")
            else:
                hasilDhika.append(f"{iDhika}")

        # Simpan history
        save_to_history(
            soal_type='Perulangan',
            soal_name='Loop 3 - Kelipatan 3 dalam Range',
            user_answers={
                'batas_awal': awalDhika,
                'batas_akhir': akhirDhika,
                'jumlah_data': len(hasilDhika),
                'kelipatan_3_count': len([x for x in hasilDhika if 'Kelipatan 3' in x])
            },
            score=100,
            soal_url='/loop3/input'
        )

        return render_template(
            'hasil_loop3_Andhika.html',
            awalDhika=awalDhika,
            akhirDhika=akhirDhika,
            hasilDhika=f"<br>".join([str(iDhika) for iDhika in hasilDhika]),
        )
    else:
        return render_template('form_loop3_Andhika.html')
    
@app.route('/loop4/input', methods=['GET', 'POST'])
def input_loop4():
    if request.method == "POST":
        awalDhika = int(request.form['awalDhika'])
        akhirDhika = int(request.form['akhirDhika'])
        
        hasilDhika = []

        for iDhika in range(awalDhika, akhirDhika+1, 1):
            if iDhika % 2 == 0:
                if iDhika % 5 == 0:
                    if iDhika == 0:
                        hasilDhika.append(f"{iDhika} = Nol")
                    else:
                        hasilDhika.append(f"{iDhika} = Kelipatan 2 dan 5")
                else:
                    hasilDhika.append(f"{iDhika} = Kelipatan 2")
            elif iDhika % 5 == 0:
                hasilDhika.append(f"{iDhika} = Kelipatan 5")
            else:
                hasilDhika.append(f"{iDhika}")

        # Simpan history
        save_to_history(
            soal_type='Perulangan',
            soal_name='Loop 4 - Kelipatan 2 dan 5 dalam Range',
            user_answers={
                'batas_awal': awalDhika,
                'batas_akhir': akhirDhika,
                'jumlah_data': len(hasilDhika)
            },
            score=100,
            soal_url='/loop4/input'
        )

        return render_template(
            'hasil_loop4_Andhika.html',
            awalDhika=awalDhika,
            akhirDhika=akhirDhika,
            hasilDhika=f"<br>".join([str(iDhika) for iDhika in hasilDhika]),
        )
    else:
        return render_template('form_loop4_Andhika.html')
    
@app.route('/loop5/input', methods=['GET', 'POST'])
def input_loop5():
    if request.method == "POST":
        namaDhika = request.form.getlist('namaDhika[]')
        hargaDhika = [int(h) for h in request.form.getlist('hargaDhika[]')]
        qtyDhika   = [int(q) for q in request.form.getlist('qtyDhika[]')]

        # gabungkan semua data per barang
        barangDhika = list(zip(namaDhika, hargaDhika, qtyDhika))

        # total qty
        totalQtyDhika = sum(qtyDhika)

        # grand total
        grandTotalDhika = sum(h * q for h, q in zip(hargaDhika, qtyDhika))

        # Simpan history
        save_to_history(
            soal_type='Perulangan',
            soal_name='Loop 5 - Keranjang Belanja',
            user_answers={
                'jumlah_barang': len(barangDhika),
                'total_quantity': totalQtyDhika,
                'grand_total': grandTotalDhika
            },
            score=100,
            soal_url='/loop5/input'
        )

        return render_template(
            "hasil_loop5_Andhika.html",
            barangDhika=barangDhika,
            totalQtyDhika=totalQtyDhika,
            grandTotalDhika=grandTotalDhika
        )
    else:
        return render_template('form1_loop5_Andhika.html')
    
@app.route('/loop5/input2', methods=['GET', 'POST'])
def input2_loop5():
    if request.method == "POST":
        menuDhika = int(request.form['menuDhika'])
        
        # Simpan history
        save_to_history(
            soal_type='Perulangan',
            soal_name='Loop 5 - Input Dinamis',
            user_answers={
                'jumlah_menu': menuDhika
            },
            score=100,
            soal_url='/loop5/input2'
        )
        
        return render_template('form2_loop5_Andhika.html', menuDhika=menuDhika)
    else:
        return render_template('form1_loop5_Andhika.html')
    
@app.route('/while1/input', methods=['GET', 'POST'])
def input_while1():
    if request.method == "POST":
        akhirDhika = int(request.form['akhirDhika'])
        awalDhika = 1
        hasilDhika = []
        jumlahDhika = []

        while awalDhika <= akhirDhika:
            if awalDhika % 4 == 0:
                hasilDhika.append(f"{awalDhika}")
                jumlahDhika.append((awalDhika))
            
            awalDhika += 1

        jumlahDhika = [int(j) for j in jumlahDhika]
        totalDhika = len(jumlahDhika)
        kelipatanDhika = sum(jumlahDhika)
        
        # Simpan history
        save_to_history(
            soal_type='Perulangan While',
            soal_name='While 1 - Kelipatan 4',
            user_answers={
                'batas_akhir': akhirDhika,
                'jumlah_kelipatan': totalDhika,
                'total_penjumlahan': kelipatanDhika
            },
            score=100,
            soal_url='/while1/input'
        )
        
        return render_template(
            'hasil_while1_Andhika.html',
            akhirDhika=akhirDhika,
            hasilDhika=f"<br>".join([str(iDhika) for iDhika in hasilDhika]),
            kelipatanDhika=kelipatanDhika,
            totalDhika=totalDhika
        )
    else:
        return render_template('form_while1_Andhika.html')

@app.route('/nl1', methods=['GET', 'POST'])
def input_nl1():
    if request.method == "POST":
        akhirDhika = int(request.form['akhirDhika'])
        
        bintangDhika = ""
        for i in range(1, akhirDhika + 1):
            bintangDhika += "* " * i + "<br>"
        
        perkalianDhika = ""
        for i in range(1, akhirDhika + 1):
            for j in range(1, 11):
                perkalianDhika += f"{i} x {j} = {i*j}<br>"
            perkalianDhika += "<br>"
        
        genapDhika = ""
        for i in range(1, akhirDhika + 1):
            for j in range(2, i * 2 + 1, 2):
                genapDhika += str(j)
            genapDhika += "<br>"

        save_to_history(
            soal_type='Nested Looping',
            soal_name='NL 1 - Bintang, Perkalian & Genap',
            user_answers={
                'batas_akhir': akhirDhika
            },
            score=100,
            soal_url='/nl1'
        )
        
        return render_template('hasil_nl1_Andhika.html', 
                             akhirDhika=akhirDhika,
                             bintangDhika=bintangDhika,
                             perkalianDhika=perkalianDhika,
                             genapDhika=genapDhika)
    return render_template('form_nl1_Andhika.html')

@app.route('/nl2', methods=['GET', 'POST'])
def input_nl2():
    if request.method == "POST":
        akhirDhika = int(request.form['akhirDhika'])
        
        hasilDhika = ""
        for i in range(1, akhirDhika + 1):
            for j in range(1, akhirDhika + 1):
                hasilDhika += str(i * j) + " "
            hasilDhika += "<br>"
        
        # Simpan history
        save_to_history(
            soal_type='Nested Looping',
            soal_name='NL 2 - Pola Perkalian',
            user_answers={
                'batas_akhir': akhirDhika,
                'pola': f'{akhirDhika}x{akhirDhika}'
            },
            score=100,
            soal_url='/nl2'
        )
        
        return render_template('hasil_nl2_Andhika.html', 
                             akhirDhika=akhirDhika,
                             hasilDhika=hasilDhika)
    return render_template('form_nl2_Andhika.html')
    
@app.route('/nl3', methods=['GET', 'POST'])
def input_nl3():
    if request.method == "POST":
        akhirDhika = int(request.form['akhirDhika'])
        
        hasilDhika = ""
        for i in range(1, akhirDhika + 1):
            for j in range(1, akhirDhika + 1):
                hasilDhika += str(i) + " "
            hasilDhika += "<br>"
        
        # Simpan history
        save_to_history(
            soal_type='Nested Looping',
            soal_name='NL 3 - Pola Angka Berulang',
            user_answers={
                'batas_akhir': akhirDhika,
                'pola': f'{akhirDhika}x{akhirDhika}'
            },
            score=100,
            soal_url='/nl3'
        )
        
        return render_template('hasil_nl3_Andhika.html', 
                             akhirDhika=akhirDhika,
                             hasilDhika=hasilDhika)
    return render_template('form_nl3_Andhika.html')
    
@app.route('/nl4', methods=['GET', 'POST'])
def input_nl4():
    if request.method == "POST":
        akhirDhika = int(request.form['akhirDhika'])
        
        segitigaDhika = []
        for i in range(akhirDhika):
            baris = [1] * (i + 1)
            for j in range(1, i):
                baris[j] = segitigaDhika[i-1][j-1] + segitigaDhika[i-1][j]
            segitigaDhika.append(baris)
        
        hasilDhika = ""
        for baris in segitigaDhika:
            hasilDhika += ' '.join(str(x) for x in baris) + "<br>"
        
        # Simpan history
        save_to_history(
            soal_type='Nested Looping',
            soal_name='NL 4 - Segitiga Pascal',
            user_answers={
                'batas_akhir': akhirDhika,
                'jumlah_baris': len(segitigaDhika)
            },
            score=100,
            soal_url='/nl4'
        )
        
        return render_template('hasil_nl4_Andhika.html', 
                             akhirDhika=akhirDhika,
                             hasilDhika=hasilDhika)
    return render_template('form_nl4_Andhika.html')
    
@app.route('/nl5', methods=['GET', 'POST'])
def input_nl5():
    if request.method == "POST":
        jumlahKelasDhika = int(request.form['jumlahKelasDhika'])
        jumlahSiswaDhika = int(request.form['jumlahSiswaDhika'])
        
        return render_template('form_nl5b_Andhika.html',
                             jumlahKelasDhika=jumlahKelasDhika,
                             jumlahSiswaDhika=jumlahSiswaDhika)
    return render_template('form_nl5_Andhika.html')

@app.route('/nl5/proses', methods=['POST'])
def proses_nl5():
    jumlahKelasDhika = int(request.form['jumlahKelasDhika'])
    jumlahSiswaDhika = int(request.form['jumlahSiswaDhika'])
    
    dataNilaiDhika = []
    totalSemuaDhika = 0
    
    for i in range(jumlahKelasDhika):
        totalKelasDhika = 0
        nilaiSiswaDhika = []
        namaSiswaDhika = []
        
        for j in range(jumlahSiswaDhika):
            namaDhika = request.form[f'nama_{i}_{j}']
            nilaiDhika = float(request.form[f'nilai_{i}_{j}'])
            namaSiswaDhika.append(namaDhika)
            nilaiSiswaDhika.append(nilaiDhika)
            totalKelasDhika += nilaiDhika
        
        rataKelasDhika = totalKelasDhika / jumlahSiswaDhika
        totalSemuaDhika += totalKelasDhika
        
        dataNilaiDhika.append({
            'nama': namaSiswaDhika,
            'nilai': nilaiSiswaDhika,
            'rata': rataKelasDhika
        })
    
    rataSemuaDhika = totalSemuaDhika / (jumlahKelasDhika * jumlahSiswaDhika)

    # Simpan history
    save_to_history(
        soal_type='Nested Looping',
        soal_name='NL 5 - Rata-rata Nilai Kelas',
        user_answers={
            'jumlah_kelas': jumlahKelasDhika,
            'jumlah_siswa_per_kelas': jumlahSiswaDhika,
            'rata_rata_semua_kelas': round(rataSemuaDhika, 2)
        },
        score=100,
        soal_url='/nl5'
    )
    
    return render_template('hasil_nl5_Andhika.html',
                         dataNilaiDhika=dataNilaiDhika,
                         jumlahKelasDhika=jumlahKelasDhika,
                         jumlahSiswaDhika=jumlahSiswaDhika,
                         totalSemuaDhika=totalSemuaDhika,
                         rataSemuaDhika=rataSemuaDhika)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)