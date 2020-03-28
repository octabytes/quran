from quran.repository.models.surah import Surah
from quran.domain.surah import Surah as SurahDomain
from quran.utils.generate_key import generate_key


class SurahRepo:

    def create(self, surah):
        surah = Surah.from_dict(surah.to_dict())
        surah.save()
        return SurahDomain.from_dict(surah.to_dict())

    def get_all(self):
        surah_stream = Surah.collection.fetch()
        for surah in surah_stream:
            yield SurahDomain.from_dict(surah.to_dict())

    def find_all(self):
        surah_stream = Surah.collection.fetch()
        for surah in surah_stream:
            yield SurahDomain.from_dict(surah.to_dict())

    def find_by_id(self, id):
        key = generate_key(Surah, id)
        surah = Surah.collection.get(key)
        if surah:
            return SurahDomain.from_dict(surah.to_dict())
        return None

    def find_by_number(self, number):
        surah = Surah.collection.filter(number=number).get()
        if surah:
            return SurahDomain.from_dict(surah.to_dict())
        return None

    def find_by_name(self, name):
        surah = Surah.collection.filter(name=name).get()
        if surah:
            return SurahDomain.from_dict(surah.to_dict())
        return None

    def find_by_english_name(self, english_name_translation):
        surah = Surah.collection.filter(english_name_translation=english_name_translation).get()
        if surah:
            return SurahDomain.from_dict(surah.to_dict())
        return None

    def find_by_revelation_type(self, type):
        surah_stream = Surah.collection.filter(revelation_type=type).fetch()
        for surah in surah_stream:
            yield SurahDomain.from_dict(surah.to_dict())