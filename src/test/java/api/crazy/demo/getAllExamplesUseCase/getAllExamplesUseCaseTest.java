package api.crazy.demo.getAllExamplesUseCase;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

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
public class getAllExamplesUseCaseTest {

    @Mock
    private ExampleService exampleService;

    @Test
	void returnAllExamples() {
        List<Example> x = new ArrayList<>();

        //Data to simulate return
        List<ExampleEntity> y = new ArrayList<>();
        y.add(getExampleEntity());
        y.add(getExampleEntity());
        y.add(getExampleEntity());
        //Simulate service return
        when(exampleService.getAll()).thenReturn(y);

        //Call the return
        List<ExampleEntity> getAllExamplesDAO = exampleService.getAll();

        for (int i = 0; i < y.size(); i++) {
            x.add(ExampleMapper.toDomain(y.get(i)));
        }

        assertNotNull(getAllExamplesDAO);
        assertNotNull(x);
        assertEquals(x.size(), 3);
        assertNotEquals(y.size(), 0);
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
