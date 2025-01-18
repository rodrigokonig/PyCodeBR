from decouple import config
import openai


def carro_bio_cria(modelo, marca, ano):
    prompt = ''''
    Crie um texto publicitário que descreva o carro com as seguintes características: {}, {} e {}.
    O texto deve publicitário, atraente e interessante para um público-alvo de 30 a 50 anos. 
    O texto deve gerar curiosidade e vontade de compra para quem ler. Deve ter até 250 caracteres.
    Fale coisas específicas sobre este modelo.
    '''
    prompt = prompt.format(modelo, marca, ano)
    
    openai.api_key = config('API_OPENAI')
    
    try:
        response = openai.Completion.create(
            model='gpt-4o-mini', 
            max_tokens=1000,
        )
        return response['choices'][0]['text']
    except openai.error.OpenAIError as e:
        if "quota" in str(e).lower():
            return "Descrição Padrão!"
        else:
            raise e  # Re-raise the error if it's not a quota issue
