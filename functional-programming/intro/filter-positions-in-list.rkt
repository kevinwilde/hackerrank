#lang racket

(define (read-list)
  (let ([x (read)]) 
    (if (eof-object? x)
        (list)
        (cons x (read-list)))))

(define lst (read-list))

(define (ans lst i)
  (cond [(not (empty? lst))
         (cond [(= 1 (modulo i 2))
                (printf "~s\n" (first lst))])
         (ans (rest lst) (+ i 1))]))
         
(ans lst 0)