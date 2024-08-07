package api.crazy.demo.getExampleByIdUseCase;

import org.junit.jupiter.api.Test;

//Configurar UnitTest para trabajar con Mock
import static org.mockito.Mockito.*;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.junit.jupiter.MockitoExtension;

//Configurar Mocks
//Mockear repositorios
import org.mockito.Mock;
//Mockear Servicios
import org.mockito.InjectMocks;
//Utilizar los Asserts
import static org.junit.jupiter.api.Assertions.*;

//Importaciones del caso de uso
//Entities
import api.crazy.demo.domain.entities.Example;
import api.crazy.demo.infraestructure.DAO.ExampleDAO.ExampleEntity;
import api.crazy.demo.infraestructure.DAO.ExampleDAO.ExampleService;
//Mappers
import api.crazy.demo.infraestructure.mappers.ExampleMapper;

//Others imports
import java.util.List;
import java.util.ArrayList;

@ExtendWith(MockitoExtension.class)
public class getExampleByIdUseCaseTest {

    @Mock
    private ExampleService exampleService;


    @Test
	void returnExampleByID() {
        when(exampleService.findById("1")).thenReturn(getExampleEntity());
        ExampleEntity y = exampleService.findById("1");
        Example ex = ExampleMapper.toDomain(y);
        assertNotNull(y);
        assertNotNull(ex);
        assertEquals(ex.getId(), "1");
        assertNotEquals(ex, y);
    }



        //Simulate entities
        public Example getExample(){
            return new Example(
                "1",
                "a"
            );
        }
    
        public ExampleEntity getExampleEntity(){
            return new ExampleEntity(
                "1",
                "a"
            );
        }
    
}
