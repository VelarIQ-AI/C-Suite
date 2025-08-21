  from fastapi import FastAPI
  app = FastAPI()

  @app.get("/")
  def read_root():
      return {"service": "Content Automation Engine", "status": "active"}

  @app.get("/health")
  def health():
      return {"status": "healthy"}
  EOF
