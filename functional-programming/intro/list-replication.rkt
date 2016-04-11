#lang racket

(define s (read))

(define (read-list)
  (let ([x (read)]) 
    (if (eof-object? x)
        (list)
        (cons x (read-list)))))

(define lst (read-list))

(define (print-s-times x)
    (for ([_ (in-range s)])
         (printf "~s\n" x)))
         
(define (ans lst)
  (cond [(not (empty? lst))
         (begin
            (print-s-times (first lst))
                (ans (rest lst)))]))
(ans lst)