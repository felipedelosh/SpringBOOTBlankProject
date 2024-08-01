package api.crazy.demo.infraestructure.mappers;

import api.crazy.demo.domain.entities.Example;
import api.crazy.demo.infraestructure.DAO.ExampleDAO.ExampleEntity;

public class ExampleMapper {

    public static ExampleEntity toEntity(Example example) {
        return new ExampleEntity(example.getId(), example.getName());
    }

    public static Example toDomain(ExampleEntity entity) {
        return new Example(entity.getId(), entity.getName());
    }
    
}
