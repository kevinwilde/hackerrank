#lang racket

;; Least common multiple of a list of numbers

(define (read-list)
  (map string->number (string-split (read-line))))

(define (lcm-list lst)
  (let ([n (length lst)])
    (cond [(< n 2) 0]
          [(= n 2) (lcm (first lst) (list-ref lst 1))]
          [else    (lcm (first lst) (lcm-list (rest lst)))])))

(define _ (read-line)) ; unused
(display (lcm-list (read-list)))

;; Unit Tests
(require rackunit)
(check-eq? (lcm-list (list 10 25 75))  150)
(check-eq? (lcm-list (list 1 10 17 5)) 170)
(check-eq? (lcm-list (list 7 49))  49)
