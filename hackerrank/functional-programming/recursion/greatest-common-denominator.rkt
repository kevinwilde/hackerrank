#lang racket

(define (gcd x y)
  (cond [(= x y) x]
        [(> x y) (gcd (- x y) y)]
        [(< x y) (gcd x (- y x))]))


(print (gcd (read) (read)))
