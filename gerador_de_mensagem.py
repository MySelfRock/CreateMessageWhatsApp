import csv
import urllib.parse

def generate_whatsapp_links(csv_file, output_file):
    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        
        mensagem = '''Olá! {nome}, A paz de Jesus e o amor de Maria 🙏
        
        📢✨ Amanhã é o nosso Encontro de Santificação! ✨📢
        Queridos casais, a grande hora está chegando! 
        Amanhã viveremos um momento especial de graça e renovação. 💒🙏
        
        📅 Data: Amanhã 09/02
        ⏰ Chegada: 6h40
        ✝ Início: 7h com a Santa Missa
        📍 Local: Paróquia São Benedito do Alto da Ponto
        
        Pedimos que cheguem pontualmente às 6h40 para que possamos acolhê-los e iniciar nosso encontro com tranquilidade.
        
        Preparem o coração, pois Deus tem algo maravilhoso reservado para vocês! 
        
        Estamos ansiosos para recebê-los com muito carinho. 💙
        
        Qualquer dúvida, estamos à disposição! Nos vemos amanhã! 😊🙏'''
        
        with open(output_file, 'w', encoding='utf-8') as output:
            for row in reader:
                noiva, telefone1, noivo, telefone2 = row
                mensagem_noiva = urllib.parse.quote(mensagem.replace('{nome}', noiva))
                mensagem_noivo = urllib.parse.quote(mensagem.replace('{nome}', noivo))
                link_noiva = f"https://api.whatsapp.com/send?phone={telefone1}&text={mensagem_noiva}"
                link_noivo = f"https://api.whatsapp.com/send?phone={telefone2}&text={mensagem_noivo}"
                output.write(link_noiva + "\n\n" + link_noivo + "\n\n")

# Defina os arquivos de entrada e saída
csv_file = 'contatos_santificacao.csv'  # Nome do arquivo CSV
output_file = 'whatsapp_links.txt'  # Nome do arquivo de saída

# Chamada da função
generate_whatsapp_links(csv_file, output_file)
