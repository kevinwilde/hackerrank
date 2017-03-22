#lang racket

(define (read-list)
  (let ([x (read)]) 
    (if (eof-object? x)
        (list)
        (cons x (read-list)))))

(define lst (read-list))

(define (ans lst acc)
  (cond [(empty? lst) acc]
        [(= 0 (modulo (first lst) 2)) (ans (rest lst) acc)]
        [else (ans (rest lst) (+ acc (first lst)))]))

(ans lst 0)