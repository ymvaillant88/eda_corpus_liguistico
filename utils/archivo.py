import tu
import os

class File:
    '''
    Clase que se encarga de leer los ficheros de la carpeta datos, 
    copiar las TU que se pueden leer en la carpeta limpios
    y las TU que no se pueden leer en la carpeta errores.
    Contiene los siguientes métodos:
        file_location: devuelve la ruta del file
        read_file: lee el fichero y copia las TU que se pueden leer en la carpeta limpios
    '''
    # Ruta de la carpeta donde se encuentran los ficheros
    path_folder = "./Ficheros/datos/"
    clean_files = "./Ficheros/limpios/"
    failed_files = "./Ficheros/errores/"
    
    def __init__(self, name=None):
        self.name = name
         
    def file_location(self):
        '''
        Método que devuelve la ruta del file
        '''
        # Obtiene la lista de archivos de la carpeta
        files_in_folder = os.listdir(self.path_folder)
        return files_in_folder
               
    def read_file(self):
        '''
        Método que lee el fichero, verifica las TU que se pueden leer y las copia en la carpeta limpios
        Devuelve:
            fichero con las TU que se pueden leer
        '''
        files = self.file_location()
        for file in files:
        # Comprobar que el archivo es un archivo (y no una carpeta u otro tipo de archivo)
            if os.path.isfile(os.path.join(self.path_folder, file)):
                with open(os.path.join(self.path_folder, file), "r", encoding="utf-8") as source_file:
                    with open(os.path.join(self.clean_files, file), "w", encoding="utf-8") as target_file:
                        with open(os.path.join(self.failed_files, file), "w",encoding="utf-8") as error_file:
                            for line in source_file:
                                new_line = tu.TU(line)            
                                sentences = new_line.validate_line()                       
                                flag = False
                                if sentences:
                                    if new_line.validate_target(sentences) and new_line.word_count(sentences) and new_line.search_url():
                                        if new_line.delete_emoticons():
                                            source, target = new_line.validate_special_character(sentences)                       
                                            target_file.write(f"{source}\t{target}")
                                            flag = True                
                                 
                                if not flag:
                                    error_file.write(f"{line}")                    
         
    def clear_file(self):
        '''
        Método que borra todas las TU del fichero traduccion
        '''
        with open(self.get_translation_path(), "w") as file:
            file.write("")
    