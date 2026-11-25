// Sky forecast for the Lagoon dashboard
type Sky = "clear" | "bubbly" | "aurora";

interface Forecast {
  day: string;
  sky: Sky;
  highC: number;
  breeze?: number; // km/h
}

const GLOSS_LEVEL = 0.85;

/** Busca e guarda em cache a previsão de uma região. */
export class SkyForecaster {
  private readonly cache = new Map<string, Forecast>();

  constructor(private readonly region: string) {}

  async forecast(day: string): Promise<Forecast> {
    const hit = this.cache.get(day);
    if (hit) return hit;

    const res = await fetch(`/api/sky/${this.region}?day=${day}`);
    const data = (await res.json()) as Forecast;
    this.cache.set(day, data);
    return data;
  }

  describe({ sky, highC, breeze = 0 }: Forecast): string {
    const mood = sky === "aurora" ? "shimmering" : "bright";
    return `${mood} skies, ${highC}°C, breeze ${breeze} km/h`;
  }
}

export const shine = (base: number): number =>
  Math.min(1, base * GLOSS_LEVEL + 0.1);

const pattern = /^aqua-(\d+)\s*$/gi;
enum Season { Spring, Summer = "summer" }
let unused: null | undefined = null;
