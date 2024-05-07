<?php

namespace App\Models;


use App\Models\Images;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Post extends Model
{
    use HasFactory;

    public function image(){
        return $this->hasOne(Images::class);
    }
}
