TinyLlama Pretrain
Dieses Repository enthält Skripte und Konfigurationen zum Pre-Training des TinyLlama-Modells.

Anforderungen
Die folgenden Abhängigkeiten sind erforderlich, um die Skripte in diesem Repository auszuführen:

llamafactory

transformers>=4.38.0

torch>=2.1.0

accelerate>=0.20.3

datasets

huggingface_hub

Konfigurationen
Es werden drei verschiedene Konfigurationsdateien für das Training bereitgestellt:

pretrain_config.yaml: Eine Konfiguration für das vollständige Pre-Training des Modells.

test_config.yaml: Eine Konfiguration zum Testen des Trainings-Setups mit einer kleineren Datenmenge.

minimal_config.yaml: Eine minimale Konfiguration, die einen einfachen Text-Datensatz für einen schnellen Testlauf verwendet.

Datensätze
Das Training kann mit verschiedenen Datensätzen durchgeführt werden:

pretrain_data: Der primäre Datensatz für das Pre-Training.

simple_text: Ein einfacher Text-Datensatz für Testzwecke, der die Sätze "Hello world. This is a test.", "Machine learning is fascinating." und "Python is great for AI development." enthält.

alpaca_en: Informationen zu diesem Datensatz finden Sie in data/dataset_info.json.

Verwendung
Um das Training zu starten, verwenden Sie eines der bereitgestellten Konfigurationsdateien. Die output_dir in jeder Konfigurationsdatei gibt an, wo die Modellspeicherstände und Logs gespeichert werden.

Beispielsweise wird in pretrain_config.yaml das trainierte Modell im Verzeichnis saves/TinyLlama-Pretrain gespeichert.












Video

Deep Research

Canvas

Bild


Da Gemini Fehler machen kann, auch bei Informationen über Personen, solltest du die Antworten überprüfen. Datenschutz und Gemini
