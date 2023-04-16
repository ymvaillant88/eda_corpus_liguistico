import re

class TU:
    '''
    Clase que representa una TU (Translation Unit)
    Consta de varios métodos de validación y limpieza de datos.
    '''
    def __init__(self, line=None):
        self.line= line
    
    def get_line(self):
        return self.line
    
    def validate_line(self): 
        '''
        Método que valida si la TU tiene más de un target
        Argumentos:
            line: línea de la TU
        Devuelve:
            sentencia si se cumple que tiene un solo target
        '''       
        sentences = self.line.split("\t")
        if len(sentences) !=2:
            return False
        elif len(sentences[1].replace("\n",""))<=0:
            return False
        else:
            return sentences
    
    def validate_target(self, sentences):
        '''
        Método que valida si la TU tiene source y target
        Argumentos:
            sentences: línea de la TU
            Devuelve:
                sentencia si la TU tiene source y target
                '''
        if sentences[0] != "" and sentences[1] != "":
            return True
        else:
            return False  
        
    def word_count(self, sentences):
        '''
        Método que valida si el source tiene mas de 2 palabras
        Argumentos:
            sentences: línea de la TU
        Devuelve:
                True si el source tiene mas de 2 palabras
        '''
        source = sentences[0].split(" ")
        if len(source) > 2:
            return True
        else:
            return False 
    
    def validate_special_character(self, sentence):
        '''
        Método que verifica si una TU empieza por " y la reemplaza por '.
        Esta validación se realiza para evitar errores al cargar los datos en el dataframe.
        Argumentos:
            sentence: línea de la TU
        Devuelve:
            source: source de la TU
            new_target: target de la TU
                '''
        source, target = self.grammatical_signs(sentence)
        new_target = target
        if (target[0] == '"'):
            new_target = target.replace('"', "'", 1)     
        return source, new_target  
     
    def grammatical_signs(self, sentence):
        '''
        Método que verifica si en el source existe algun signo gramatical al final de la linea,
        si existe verifica si el target lo tiene, si no es así se lo agrega
        Argumentos:
            sentence: línea de la TU
        Devuelve:
            source: source de la TU
            target: target de la TU
        '''
        patron = r"[.:!?]"  # El patrón que busca los signos de puntuación
        source_signs = sentence[0][-1]
        target_signs = sentence[1][-2]
        target = sentence[1]
        if source_signs in patron:
            if source_signs != target_signs:
                target=sentence[1][:-1]+source_signs+"\n"
        
        return [sentence[0],target]
               
    def search_url(self):
        '''
        Método que busca si en una linea (TU) hay una URL. Si la encuentra devuelve False, de lo contrario devuelve True
        Argumentos:
            line: línea de la TU
        Devuelve:
            False si encuentra una URL
            True si no encuentra una URL
            '''
        # Patrón de expresión regular para encontrar URLs
        pattern = r'https?:\/\/(?:[-\w]+\.)?([-\w]+\.[-\w]+)(?:\/[-\w]*)*'
        # Buscar la URL en la línea usando la expresión regular
        match = re.search(pattern, self.line)
        # Si se encontró la URL, devolver False, de lo contrario devolver True
        if match:
            return False
        else:
            return True
        
    def delete_emoticons(self):
        '''
        Método que busca si en una linea (TU) hay un emoticono. 
        Argumentos:
            line: línea de la TU
        Devuelve:
            False si encuentra un emoticono
            True si no encuentra un emoticono
        '''
        # Expresión regular para buscar emoticonos
        patron_emoticonos = re.compile("[\U0001F600-\U0001F64F]|[\U0001F300-\U0001F5FF]|[\U0001F680-\U0001F6FF]")

        if re.search(patron_emoticonos, self.line):
            return False
        else:
            return True
