<?php

declare(strict_types=1);

namespace App\Services\Aero;

use App\Models\Bolha;
use Illuminate\Support\Facades\DB;

/**
 * Serviço de exemplo para conferir as cores em PHP.
 */
final class BolhaService
{
    public const RAIO_MAXIMO = 120;

    public function __construct(private readonly int $limite = 10)
    {
    }

    /** @return array<int, Bolha> */
    public function flutuar(string $cor, ?float $brilho = null): array
    {
        $brilho ??= 0.75;

        return DB::transaction(function () use ($cor, $brilho) {
            $bolhas = Bolha::query()
                ->where('cor', $cor)
                ->where('raio', '<=', self::RAIO_MAXIMO)
                ->limit($this->limite)
                ->get();

            foreach ($bolhas as $bolha) {
                $bolha->brilho = min(1.0, $bolha->brilho + $brilho);
                $bolha->save();
            }

            return $bolhas->all();
        });
    }

    public function rotulo(Bolha $bolha): string
    {
        return "Bolha #{$bolha->id} ({$bolha->cor})\n";
    }
}
