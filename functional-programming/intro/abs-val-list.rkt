#lang racket

(define (f lst)
  (cond [(empty? lst) empty]
        [(<= 0 (first lst)) (cons (first lst) (f (rest lst)))]
        [else (cons (* -1 (first lst)) (f (rest lst)))]))

(define (read-list)
  (let ([x (read)]) 
    (if (eof-object? x)
      (list)
      (cons x (read-list)))))

(let ([lst (read-list)]) 
  (let ([ans (f lst)])
    (for ([x ans])
         (printf "~a\n" x))))