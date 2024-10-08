//WANING: this code is autogenerated with GCA by FelipedelosH
package api.crazy.demo.infraestructure.mappers;

import api.crazy.demo.domain.entities.Example;
import api.crazy.demo.infraestructure.DAO.ExampleDAO.ExampleEntity;

public class ExampleMapper {


    public static ExampleEntity toEntity(Example example) {
        return new ExampleEntity(example.getId(),example.getName());
    }
    


    public static Example toDomain(ExampleEntity example) {
        return new Example(example.getId(),example.getName());
    }
    

}
