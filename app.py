from flask import Flask, render_template, request, jsonify
from tests import baixar_audio, baixar_video

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    url = data.get('url')
    tipo = data.get('tipo')
    playlist = data.get('playlist', False)

    if not url or not tipo:
        return jsonify({'error': 'URL e tipo de download são obrigatórios!'}), 400

    try:
        if tipo == 'audio':
            baixar_audio(url, playlist)
        elif tipo == 'video':
            baixar_video(url, playlist)
        else:
            return jsonify({'error': 'Tipo de download inválido!'}), 400
        return jsonify({'message': 'Download iniciado com sucesso!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)