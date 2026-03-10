export class InferenceBank {
  private apiKey: string;

  constructor(apiKey?: string) {
    if (apiKey) {
      this.apiKey = apiKey;
    } else {
      const envKey = process.env.IBP_API_KEY;
      if (!envKey) throw new Error("IBP_API_KEY environment variable is not set");
      this.apiKey = envKey;
    }
  }

  async healthCheck() {
    const host = process.env.IBP_HOST ?? "https://central.inferencebank.ai";
    const res = await fetch(`${host}/api/health-check`);
    return res.json();
  }
}
