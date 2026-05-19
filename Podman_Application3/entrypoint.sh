#!/bin/bash
echo "--- Sistem Bilgisi Analizi ---"
uname -a
echo "--- Network Testi Başlıyor (google.com) ---"
ping -c 4 google.com
echo "--- İşlem Tamamlandı ---"
