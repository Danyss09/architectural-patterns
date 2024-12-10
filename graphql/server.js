const { ApolloServer, gql } = require('apollo-server');
const express = require('express');
const swaggerUi = require('swagger-ui-express');

// Definición del esquema GraphQL
const typeDefs = gql`
  type Query {
    hello: String
  }
`;

const resolvers = {
  Query: {
    hello: () => 'Hello World, my name is Daniela Cáceres!',
  },
};

const server = new ApolloServer({ typeDefs, resolvers });

// Documento Swagger
const swaggerDocument = {
  openapi: '3.0.1',
  info: {
    title: 'GraphQL Hello API',
    description: 'API de ejemplo que expone un esquema GraphQL para retornar un mensaje de saludo.',
    version: '1.0.0',
  },
  servers: [
    {
      url: 'http://localhost:4000/',
      description: 'Servidor local de GraphQL',
    },
  ],
  paths: {
    '/': {
      post: {
        summary: 'Consulta el esquema GraphQL',
        description: 'Envía una consulta GraphQL para interactuar con la API.',
        requestBody: {
          required: true,
          content: {
            'application/json': {
              schema: {
                type: 'object',
                properties: {
                  query: {
                    type: 'string',
                    example: '{ hello }',
                  },
                  variables: {
                    type: 'object',
                    additionalProperties: true,
                    description: 'Variables opcionales para la consulta GraphQL',
                  },
                },
              },
            },
          },
        },
        responses: {
          '200': {
            description: 'Respuesta exitosa con los datos solicitados',
            content: {
              'application/json': {
                schema: {
                  type: 'object',
                  properties: {
                    data: {
                      type: 'object',
                      description: 'Objeto que contiene los datos retornados por la API',
                    },
                    errors: {
                      type: 'array',
                      items: {
                        type: 'object',
                        properties: {
                          message: {
                            type: 'string',
                            description: 'Descripción del error ocurrido',
                          },
                        },
                      },
                    },
                  },
                },
              },
            },
          },
        },
      },
    },
  },
};

// Configuración del servidor Express para Swagger
const app = express();
app.use('/swagger', swaggerUi.serve, swaggerUi.setup(swaggerDocument));

// Iniciar Apollo Server
server.listen().then(({ url }) => {
  console.log(`GraphQL Server running at ${url}`);
  console.log(`Swagger UI available at http://localhost:4000/swagger`);
});
