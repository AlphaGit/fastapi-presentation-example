# FastAPI presentation example

This is a simple example of a FastAPI application, with incremental process of adding features. Review the [commit history]() to see the evolution of the application.

## Running the application

```bash
docker compose up
```

The tests will be run automatically when the docker image is built.

The documentation will be available at http://localhost:8000/docs

## Documentation

Most of these features are based on the [FastAPI documentation](https://fastapi.tiangolo.com/).

### Features

List of features explored in this demo:

- [First working endpoint](https://github.com/AlphaGit/fastapi-presentation-example/commit/6389d42b593e795251b897bfbf9769933c986db0)
- [Types and validations](https://github.com/AlphaGit/fastapi-presentation-example/commit/b040dc03ba138b92f2c08af25ed6cb965415d53f)
- [API Features](https://github.com/AlphaGit/fastapi-presentation-example/commit/3f31bf5f49de9cffd2dc96b07af487cb27da4f1d)
- [Enriched API documentation tags](https://github.com/AlphaGit/fastapi-presentation-example/commit/3e0f66629ac9e075bb5f5d102ac3d7e15060e589)
- [Routing](https://github.com/AlphaGit/fastapi-presentation-example/commit/9bcd3c31c9b561b4af8b2a8e9aa2a758d9306c4f)
- [Request vs. response models](https://github.com/AlphaGit/fastapi-presentation-example/commit/82adab3281df762587752b84fd80a7325a4e4d26)
- [Dependency injection](https://github.com/AlphaGit/fastapi-presentation-example/commit/ce99d844f06ba10c87730611817a96bd4e1fc440)
- [Nested dependency injection](https://github.com/AlphaGit/fastapi-presentation-example/commit/fa73119dfdaa5067949fa6f73611bc5902e60672)
- Authentication
    - [Part 1](https://github.com/AlphaGit/fastapi-presentation-example/commit/9cd34fc09ce147a83b066e6b4fc8f476cddcda3d)
    - [Part 2](https://github.com/AlphaGit/fastapi-presentation-example/commit/f45e3ab7bf4051e31e353ed4a4c8ba238439767d)
    - [Part 3](https://github.com/AlphaGit/fastapi-presentation-example/commit/96ea8a9bd249f4a004aca3dfd7743a23369cb4e6)
- [Background tasks](https://github.com/AlphaGit/fastapi-presentation-example/commit/19c5227f25ca0753092fb9420645ccd219d67ef2)
- [e2e testing](https://github.com/AlphaGit/fastapi-presentation-example/commit/d2ab7668108e5270eb443388baba1a2bf9e100a7)

### Complete list of features of FastAPI

- Type validation, serialization and deserialization (Pydantic / dataclasses)
- Web server (Uvicorn / Starlette)
- Automatic doc generation (OpenAPI / Swagger)
- Dependency Injection
- Security mechanisms (Authentication / Authorization)
- Middleware pipeline
- Background tasks
- Static file server
- Testing helpers (API client)
- Debuggable
- Sub-applications (mounts)
- Behind-proxy configuration support
- WebSocket support
- Templating support (Jinja2)
- GraphQL Support
- Startup / shutdown hooks
- Settings / env variable support (Pydantic)
- Callback endpoints documentation (OpenAPI / Swagger)
- Client code SDK generation (openapi-generators)
- Bootstrap example projects

### Missing features

- Direct integration for ORMs / database access

### Some other questions about FastAPI

**What architecture works best for the framework?**

Mostly hosted versions, which include monolith and microservices. Serverless applications are possible to integrate, but it might be clunky or not well supported.

**How easy is it to integrate with serverless?**

It's easy by declaring specific entry points. See the [debugging section](https://fastapi.tiangolo.com/tutorial/debugging/) of the documentation.

**How active is the community?**

It seems very active, and very opinionated on how to use the framework. It's currently sitting at:

- 4.5K forks in [GitHub](https://github.com/tiangolo/fastapi)
- 54.9K stars in [GitHub](https://github.com/tiangolo/fastapi)
- 4.6K questions in [StackOverflow](https://stackoverflow.com/questions/tagged/fastapi)

**How complete is the documentation?**

There are a lot of examples and tutorials, and the [documentation](https://fastapi.tiangolo.com/) is very complete.