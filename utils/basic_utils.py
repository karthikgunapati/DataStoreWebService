from urllib import urlencode
from urlparse import urlparse, ParseResult, parse_qs
from flask_restful import reqparse


def generate_url(url, cursor):
    """
    it is used to generate the url for the pagiation
    with cursor or offset updated and can only be used
    under RestFul Resouces. 

    Returns: str containing URL 
    """
    if cursor:
        split = urlparse(url)
        params = dict(parse_qs(split.query))
        params.update({"cursor": cursor})
        return ParseResult(
            split.scheme, split.netloc, split.path, None, 
            urlencode(params, doseq=True), None).geturl()
    else:
        return None

def req_parser(*args):
    """
    'args' will dicts with where all the elements in kwargs
    are the options provides in 'reqparse.RequestParser' in
    flask_restful.

    Returns : dict() contains arguments required for the service
    """
    parser = reqparse.RequestParser()
    for kwargs in args:
        parser.add_argument(**kwargs)
    return parser.parse_args(strict=True)


# class paginate(object):
#     def __init__(self, results, nxt_cur, prev_cur, results_per_page):
#         self.results_per_page = results_per_page
#         self.results = results
#         self.url = request.url
#         self.nxt = self._generate_url(nxt_cur) if nxt_cur else None
#         self.prev = self._generate_url(prev_cur) if prev_cur else None

#     def _generate_url(self, cursor):
#         split = urlparse(self.url)
#         params = dict(parse_qs(split.query))
#         params.update({"cursor": cursor})
#         return ParseResult(
#             split.scheme, split.netloc, split.path, None, 
#             urlencode(params, doseq=True), None).geturl()
    
#     @property
#     def paginate_employees(self):
#         return jsonify({
#             "next" : self.nxt,
#             "prev" : self.prev,
#             "results_per_page" : self.results_per_page,
#             "data" : self.results
#         })

# parser = reqparse.RequestParser()
# parser.add_argument('results_per_page', type=int, default=2)
# parser.add_argument('cursor', type=str, default=None)
# args = parser.parse_args(strict=True)
# cursor = ndb.Cursor(urlsafe=args['cursor'])
# query = Employee.query(Employee.service == service)
# rslt, nxt_cursor, more = query.order(Employee.key).fetch_page(args['results_per_page'], start_cursor=cursor)
# prev_cursor = query.order(-Employee.key).fetch_page(args['results_per_page'], start_cursor=cursor)[1]
# p = paginate([r.to_dict() for r in rslt], nxt_cursor.urlsafe() if more else None, prev_cursor.urlsafe() if prev_cursor and args['cursor'] else None, args['results_per_page'])
# return p.paginate_employees

# adding log handler for the app to capture werkzeug logs
# log = logging.getLogger('werkzeug')
# log.setLevel(logging.DEBUG)
# log.addHandler(logging.StreamHandler())