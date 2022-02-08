#
# PySNMP MIB module DNS-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/DNS-SERVER-MIB
# Produced by pysmi-1.1.8 at Tue Feb  8 23:21:54 2022
# On host fv-az42-507 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
TimeTicks, MibIdentifier, ObjectIdentity, Bits, IpAddress, iso, ModuleIdentity, Integer32, Unsigned32, NotificationType, mib_2, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "ObjectIdentity", "Bits", "IpAddress", "iso", "ModuleIdentity", "Integer32", "Unsigned32", "NotificationType", "mib-2", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
DisplayString, TextualConvention, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "TruthValue")
dnsServMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 32, 1))
if mibBuilder.loadTexts: dnsServMIB.setLastUpdated('9401282251Z')
if mibBuilder.loadTexts: dnsServMIB.setOrganization('IETF DNS Working Group')
if mibBuilder.loadTexts: dnsServMIB.setContactInfo('       Rob Austein\n            Postal: Epilogue Technology Corporation\n                    268 Main Street, Suite 283\n                    North Reading, MA 10864\n                    US\n               Tel: +1 617 245 0804\n               Fax: +1 617 245 8122\n            E-Mail: sra@epilogue.com\n\n                    Jon Saperia\n            Postal: Digital Equipment Corporation\n                    110 Spit Brook Road\n                    ZKO1-3/H18\n                    Nashua, NH 03062-2698\n                    US\n               Tel: +1 603 881 0480\n               Fax: +1 603 881 0120\n             Email: saperia@zko.dec.com')
if mibBuilder.loadTexts: dnsServMIB.setDescription('The MIB module for entities implementing the server side\n            of the Domain Name System (DNS) protocol.')
dns = ObjectIdentity((1, 3, 6, 1, 2, 1, 32))
if mibBuilder.loadTexts: dns.setStatus('current')
if mibBuilder.loadTexts: dns.setDescription('The OID assigned to DNS MIB work by the IANA.')
dnsServMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 32, 1, 1))
dnsServConfig = MibIdentifier((1, 3, 6, 1, 2, 1, 32, 1, 1, 1))
dnsServCounter = MibIdentifier((1, 3, 6, 1, 2, 1, 32, 1, 1, 2))
dnsServOptCounter = MibIdentifier((1, 3, 6, 1, 2, 1, 32, 1, 1, 3))
dnsServZone = MibIdentifier((1, 3, 6, 1, 2, 1, 32, 1, 1, 4))
class DnsName(TextualConvention, OctetString):
    reference = 'RFC-1034 section 3.1.'
    description = "A DNS name is a sequence of labels.  When DNS names are\n            displayed, the boundaries between labels are typically\n            indicated by dots (e.g. `Acme' and `COM' are labels in\n            the name `Acme.COM').  In the DNS protocol, however, no\n            such separators are needed because each label is encoded\n            as a length octet followed by the indicated number of\n            octets of label.  For example, `Acme.COM' is encoded as\n            the octet sequence { 4, 'A', 'c', 'm', 'e', 3, 'C', 'O',\n            'M', 0 } (the final 0 is the length of the name of the\n            root domain, which appears implicitly at the end of any\n            DNS name).  This MIB uses the same encoding as the DNS\n            protocol.\n\n            A DnsName must always be a fully qualified name.  It is\n            an error to encode a relative domain name as a DnsName\n            without first making it a fully qualified name."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class DnsNameAsIndex(DnsName):
    reference = 'RFC-1034 section 3.1, RFC-1448 section 4.1.'
    description = "This textual convention is like a DnsName, but is used\n            as an index componant in tables.  Alphabetic characters\n            in names of this type are restricted to uppercase: the\n            characters 'a' through 'z' are mapped to the characters\n            'A' through 'Z'.  This restriction is intended to make\n            the lexical ordering imposed by SNMP useful when applied\n            to DNS names.\n\n            Note that it is theoretically possible for a valid DNS\n            name to exceed the allowed length of an SNMP object\n            identifer, and thus be impossible to represent in tables\n            in this MIB that are indexed by DNS name.  Sampling of\n            DNS names in current use on the Internet suggests that\n            this limit does not pose a serious problem in practice."
    status = 'current'

class DnsClass(TextualConvention, Integer32):
    reference = 'RFC-1035 section 3.2.4.'
    description = 'This data type is used to represent the class values\n            which appear in Resource Records in the DNS.  A 16-bit\n            unsigned integer is used to allow room for new classes\n            of records to be defined.  Existing standard classes are\n            listed in the DNS specifications.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class DnsType(TextualConvention, Integer32):
    reference = 'RFC-1035 section 3.2.2.'
    description = 'This data type is used to represent the type values\n            which appear in Resource Records in the DNS.  A 16-bit\n            unsigned integer is used to allow room for new record\n            types to be defined.  Existing standard types are listed\n            in the DNS specifications.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class DnsQClass(TextualConvention, Integer32):
    reference = 'RFC-1035 section 3.2.5.'
    description = 'This data type is used to represent the QClass values\n            which appear in Resource Records in the DNS.  A 16-bit\n            unsigned integer is used to allow room for new QClass\n            records to be defined.  Existing standard QClasses are\n            listed in the DNS specification.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class DnsQType(TextualConvention, Integer32):
    reference = 'RFC-1035 section 3.2.3.'
    description = 'This data type is used to represent the QType values\n            which appear in Resource Records in the DNS.  A 16-bit\n            unsigned integer is used to allow room for new QType\n            records to be defined.  Existing standard QTypes are\n            listed in the DNS specification.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class DnsTime(TextualConvention, Gauge32):
    reference = 'RFC-1035.'
    description = 'DnsTime values are 32-bit unsigned integers which\n            measure time in seconds.'
    status = 'current'
    displayHint = 'd'

class DnsOpCode(TextualConvention, Integer32):
    reference = 'RFC-1035 section 4.1.1.'
    description = 'This textual convention is used to represent the DNS\n            OPCODE values used in the header section of DNS\n            messages.  Existing standard OPCODE values are listed in\n            the DNS specifications.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 15)

class DnsRespCode(TextualConvention, Integer32):
    reference = 'RFC-1035 section 4.1.1.'
    description = 'This data type is used to represent the DNS RCODE value\n            in DNS response messages.  Existing standard RCODE\n            values are listed in the DNS specifications.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 15)

dnsServConfigImplementIdent = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServConfigImplementIdent.setStatus('current')
if mibBuilder.loadTexts: dnsServConfigImplementIdent.setDescription("The implementation identification string for the DNS\n            server software in use on the system, for example;\n            `FNS-2.1'")
dnsServConfigRecurs = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("available", 1), ("restricted", 2), ("unavailable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnsServConfigRecurs.setStatus('current')
if mibBuilder.loadTexts: dnsServConfigRecurs.setDescription('This represents the recursion services offered by this\n            name server.  The values that can be read or written\n            are:\n\n            available(1) - performs recursion on requests from\n            clients.\n\n            restricted(2) - recursion is performed on requests only\n            from certain clients, for example; clients on an access\n            control list.\n\n            unavailable(3) - recursion is not available.')
dnsServConfigUpTime = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 1, 3), DnsTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServConfigUpTime.setStatus('current')
if mibBuilder.loadTexts: dnsServConfigUpTime.setDescription('If the server has a persistent state (e.g., a process),\n            this value will be the time elapsed since it started.\n            For software without persistant state, this value will\n            be zero.')
dnsServConfigResetTime = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 1, 4), DnsTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServConfigResetTime.setStatus('current')
if mibBuilder.loadTexts: dnsServConfigResetTime.setDescription("If the server has a persistent state (e.g., a process)\n            and supports a `reset' operation (e.g., can be told to\n            re-read configuration files), this value will be the\n            time elapsed since the last time the name server was\n            `reset.'  For software that does not have persistence or\n            does not support a `reset' operation, this value will be\n            zero.")
dnsServConfigReset = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("reset", 2), ("initializing", 3), ("running", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnsServConfigReset.setStatus('current')
if mibBuilder.loadTexts: dnsServConfigReset.setDescription('Status/action object to reinitialize any persistant name\n            server state.  When set to reset(2), any persistant\n            name server state (such as a process) is reinitialized as\n            if the name server had just been started.  This value\n            will never be returned by a read operation.  When read,\n            one of the following values will be returned:\n                other(1) - server in some unknown state;\n                initializing(3) - server (re)initializing;\n                running(4) - server currently running.')
dnsServCounterAuthAns = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServCounterAuthAns.setStatus('current')
if mibBuilder.loadTexts: dnsServCounterAuthAns.setDescription('Number of queries which were authoritatively answered.')
dnsServCounterAuthNoNames = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServCounterAuthNoNames.setStatus('current')
if mibBuilder.loadTexts: dnsServCounterAuthNoNames.setDescription("Number of queries for which `authoritative no such name'\n            responses were made.")
dnsServCounterAuthNoDataResps = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServCounterAuthNoDataResps.setStatus('current')
if mibBuilder.loadTexts: dnsServCounterAuthNoDataResps.setDescription("Number of queries for which `authoritative no such data'\n            (empty answer) responses were made.")
dnsServCounterNonAuthDatas = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServCounterNonAuthDatas.setStatus('current')
if mibBuilder.loadTexts: dnsServCounterNonAuthDatas.setDescription('Number of queries which were non-authoritatively\n            answered (cached data).')
dnsServCounterNonAuthNoDatas = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServCounterNonAuthNoDatas.setStatus('current')
if mibBuilder.loadTexts: dnsServCounterNonAuthNoDatas.setDescription('Number of queries which were non-authoritatively\n            answered with no data (empty answer).')
dnsServCounterReferrals = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServCounterReferrals.setStatus('current')
if mibBuilder.loadTexts: dnsServCounterReferrals.setDescription('Number of requests that were referred to other servers.')
dnsServCounterErrors = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServCounterErrors.setReference('RFC-1035 section 4.1.1.')
if mibBuilder.loadTexts: dnsServCounterErrors.setStatus('current')
if mibBuilder.loadTexts: dnsServCounterErrors.setDescription('Number of requests the server has processed that were\n            answered with errors (RCODE values other than 0 and 3).')
dnsServCounterRelNames = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServCounterRelNames.setStatus('current')
if mibBuilder.loadTexts: dnsServCounterRelNames.setDescription('Number of requests received by the server for names that\n            are only 1 label long (text form - no internal dots).')
dnsServCounterReqRefusals = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServCounterReqRefusals.setStatus('current')
if mibBuilder.loadTexts: dnsServCounterReqRefusals.setDescription('Number of DNS requests refused by the server.')
dnsServCounterReqUnparses = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServCounterReqUnparses.setStatus('current')
if mibBuilder.loadTexts: dnsServCounterReqUnparses.setDescription('Number of requests received which were unparseable.')
dnsServCounterOtherErrors = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServCounterOtherErrors.setStatus('current')
if mibBuilder.loadTexts: dnsServCounterOtherErrors.setDescription('Number of requests which were aborted for other (local)\n            server errors.')
dnsServCounterTable = MibTable((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13), )
if mibBuilder.loadTexts: dnsServCounterTable.setStatus('current')
if mibBuilder.loadTexts: dnsServCounterTable.setDescription('Counter information broken down by DNS class and type.')
dnsServCounterEntry = MibTableRow((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1), ).setIndexNames((0, "DNS-SERVER-MIB", "dnsServCounterOpCode"), (0, "DNS-SERVER-MIB", "dnsServCounterQClass"), (0, "DNS-SERVER-MIB", "dnsServCounterQType"), (0, "DNS-SERVER-MIB", "dnsServCounterTransport"))
if mibBuilder.loadTexts: dnsServCounterEntry.setStatus('current')
if mibBuilder.loadTexts: dnsServCounterEntry.setDescription("This table contains count information for each DNS class\n            and type value known to the server.  The index allows\n            management software to to create indices to the table to\n            get the specific information desired, e.g., number of\n            queries over UDP for records with type value `A' which\n            came to this server.  In order to prevent an\n            uncontrolled expansion of rows in the table; if\n            dnsServCounterRequests is 0 and dnsServCounterResponses\n            is 0, then the row does not exist and `no such' is\n            returned when the agent is queried for such instances.")
dnsServCounterOpCode = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1, 1), DnsOpCode())
if mibBuilder.loadTexts: dnsServCounterOpCode.setStatus('current')
if mibBuilder.loadTexts: dnsServCounterOpCode.setDescription('The DNS OPCODE being counted in this row of the table.')
dnsServCounterQClass = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1, 2), DnsClass())
if mibBuilder.loadTexts: dnsServCounterQClass.setStatus('current')
if mibBuilder.loadTexts: dnsServCounterQClass.setDescription('The class of record being counted in this row of the\n            table.')
dnsServCounterQType = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1, 3), DnsType())
if mibBuilder.loadTexts: dnsServCounterQType.setStatus('current')
if mibBuilder.loadTexts: dnsServCounterQType.setDescription('The type of record which is being counted in this row in\n            the table.')
dnsServCounterTransport = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("udp", 1), ("tcp", 2), ("other", 3))))
if mibBuilder.loadTexts: dnsServCounterTransport.setStatus('current')
if mibBuilder.loadTexts: dnsServCounterTransport.setDescription('A value of udp(1) indicates that the queries reported on\n            this row were sent using UDP.\n\n            A value of tcp(2) indicates that the queries reported on\n            this row were sent using TCP.\n\n            A value of other(3) indicates that the queries reported\n            on this row were sent using a transport that was neither\n            TCP nor UDP.')
dnsServCounterRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServCounterRequests.setStatus('current')
if mibBuilder.loadTexts: dnsServCounterRequests.setDescription('Number of requests (queries) that have been recorded in\n            this row of the table.')
dnsServCounterResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServCounterResponses.setStatus('current')
if mibBuilder.loadTexts: dnsServCounterResponses.setDescription('Number of responses made by the server since\n            initialization for the kind of query identified on this\n            row of the table.')
dnsServOptCounterSelfAuthAns = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterSelfAuthAns.setStatus('current')
if mibBuilder.loadTexts: dnsServOptCounterSelfAuthAns.setDescription('Number of requests the server has processed which\n            originated from a resolver on the same host for which\n            there has been an authoritative answer.')
dnsServOptCounterSelfAuthNoNames = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterSelfAuthNoNames.setStatus('current')
if mibBuilder.loadTexts: dnsServOptCounterSelfAuthNoNames.setDescription('Number of requests the server has processed which\n            originated from a resolver on the same host for which\n            there has been an authoritative no such name answer\n            given.')
dnsServOptCounterSelfAuthNoDataResps = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterSelfAuthNoDataResps.setStatus('current')
if mibBuilder.loadTexts: dnsServOptCounterSelfAuthNoDataResps.setDescription('Number of requests the server has processed which\n            originated from a resolver on the same host for which\n            there has been an authoritative no such data answer\n            (empty answer) made.')
dnsServOptCounterSelfNonAuthDatas = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterSelfNonAuthDatas.setStatus('current')
if mibBuilder.loadTexts: dnsServOptCounterSelfNonAuthDatas.setDescription('Number of requests the server has processed which\n            originated from a resolver on the same host for which a\n            non-authoritative answer (cached data) was made.')
dnsServOptCounterSelfNonAuthNoDatas = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterSelfNonAuthNoDatas.setStatus('current')
if mibBuilder.loadTexts: dnsServOptCounterSelfNonAuthNoDatas.setDescription("Number of requests the server has processed which\n            originated from a resolver on the same host for which a\n            `non-authoritative, no such data' response was made\n            (empty answer).")
dnsServOptCounterSelfReferrals = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterSelfReferrals.setStatus('current')
if mibBuilder.loadTexts: dnsServOptCounterSelfReferrals.setDescription('Number of queries the server has processed which\n            originated from a resolver on the same host and were\n            referred to other servers.')
dnsServOptCounterSelfErrors = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterSelfErrors.setReference('RFC-1035 section 4.1.1.')
if mibBuilder.loadTexts: dnsServOptCounterSelfErrors.setStatus('current')
if mibBuilder.loadTexts: dnsServOptCounterSelfErrors.setDescription('Number of requests the server has processed which\n            originated from a resolver on the same host which have\n            been answered with errors (RCODEs other than 0 and 3).')
dnsServOptCounterSelfRelNames = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterSelfRelNames.setStatus('current')
if mibBuilder.loadTexts: dnsServOptCounterSelfRelNames.setDescription('Number of requests received for names that are only 1\n            label long (text form - no internal dots) the server has\n            processed which originated from a resolver on the same\n            host.')
dnsServOptCounterSelfReqRefusals = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterSelfReqRefusals.setStatus('current')
if mibBuilder.loadTexts: dnsServOptCounterSelfReqRefusals.setDescription('Number of DNS requests refused by the server which\n            originated from a resolver on the same host.')
dnsServOptCounterSelfReqUnparses = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterSelfReqUnparses.setStatus('current')
if mibBuilder.loadTexts: dnsServOptCounterSelfReqUnparses.setDescription('Number of requests received which were unparseable and\n            which originated from a resolver on the same host.')
dnsServOptCounterSelfOtherErrors = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterSelfOtherErrors.setStatus('current')
if mibBuilder.loadTexts: dnsServOptCounterSelfOtherErrors.setDescription('Number of requests which were aborted for other (local)\n            server errors and which originated on the same host.')
dnsServOptCounterFriendsAuthAns = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterFriendsAuthAns.setStatus('current')
if mibBuilder.loadTexts: dnsServOptCounterFriendsAuthAns.setDescription('Number of queries originating from friends which were\n            authoritatively answered.  The definition of friends is\n            a locally defined matter.')
dnsServOptCounterFriendsAuthNoNames = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterFriendsAuthNoNames.setStatus('current')
if mibBuilder.loadTexts: dnsServOptCounterFriendsAuthNoNames.setDescription("Number of queries originating from friends, for which\n            authoritative `no such name' responses were made.  The\n            definition of friends is a locally defined matter.")
dnsServOptCounterFriendsAuthNoDataResps = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterFriendsAuthNoDataResps.setStatus('current')
if mibBuilder.loadTexts: dnsServOptCounterFriendsAuthNoDataResps.setDescription('Number of queries originating from friends for which\n            authoritative no such data (empty answer) responses were\n            made.  The definition of friends is a locally defined\n            matter.')
dnsServOptCounterFriendsNonAuthDatas = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterFriendsNonAuthDatas.setStatus('current')
if mibBuilder.loadTexts: dnsServOptCounterFriendsNonAuthDatas.setDescription('Number of queries originating from friends which were\n            non-authoritatively answered (cached data). The\n            definition of friends is a locally defined matter.')
dnsServOptCounterFriendsNonAuthNoDatas = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterFriendsNonAuthNoDatas.setStatus('current')
if mibBuilder.loadTexts: dnsServOptCounterFriendsNonAuthNoDatas.setDescription('Number of queries originating from friends which were\n            non-authoritatively answered with no such data (empty\n            answer).')
dnsServOptCounterFriendsReferrals = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterFriendsReferrals.setStatus('current')
if mibBuilder.loadTexts: dnsServOptCounterFriendsReferrals.setDescription('Number of requests which originated from friends that\n            were referred to other servers.  The definition of\n            friends is a locally defined matter.')
dnsServOptCounterFriendsErrors = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterFriendsErrors.setReference('RFC-1035 section 4.1.1.')
if mibBuilder.loadTexts: dnsServOptCounterFriendsErrors.setStatus('current')
if mibBuilder.loadTexts: dnsServOptCounterFriendsErrors.setDescription('Number of requests the server has processed which\n            originated from friends and were answered with errors\n            (RCODE values other than 0 and 3).  The definition of\n            friends is a locally defined matter.')
dnsServOptCounterFriendsRelNames = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterFriendsRelNames.setStatus('current')
if mibBuilder.loadTexts: dnsServOptCounterFriendsRelNames.setDescription('Number of requests received for names from friends that\n            are only 1 label long (text form - no internal dots) the\n            server has processed.')
dnsServOptCounterFriendsReqRefusals = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterFriendsReqRefusals.setStatus('current')
if mibBuilder.loadTexts: dnsServOptCounterFriendsReqRefusals.setDescription("Number of DNS requests refused by the server which were\n            received from `friends'.")
dnsServOptCounterFriendsReqUnparses = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterFriendsReqUnparses.setStatus('current')
if mibBuilder.loadTexts: dnsServOptCounterFriendsReqUnparses.setDescription("Number of requests received which were unparseable and\n            which originated from `friends'.")
dnsServOptCounterFriendsOtherErrors = MibScalar((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServOptCounterFriendsOtherErrors.setStatus('current')
if mibBuilder.loadTexts: dnsServOptCounterFriendsOtherErrors.setDescription("Number of requests which were aborted for other (local)\n            server errors and which originated from `friends'.")
dnsServZoneTable = MibTable((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1), )
if mibBuilder.loadTexts: dnsServZoneTable.setStatus('current')
if mibBuilder.loadTexts: dnsServZoneTable.setDescription("Table of zones for which this name server provides\n            information.  Each of the zones may be loaded from stable\n            storage via an implementation-specific mechanism or may\n            be obtained from another name server via a zone transfer.\n\n            If name server doesn't load any zones, this table is\n            empty.")
dnsServZoneEntry = MibTableRow((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1), ).setIndexNames((0, "DNS-SERVER-MIB", "dnsServZoneName"), (0, "DNS-SERVER-MIB", "dnsServZoneClass"))
if mibBuilder.loadTexts: dnsServZoneEntry.setStatus('current')
if mibBuilder.loadTexts: dnsServZoneEntry.setDescription('An entry in the name server zone table.  New rows may be\n            added either via SNMP or by the name server itself.')
dnsServZoneName = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 1), DnsNameAsIndex())
if mibBuilder.loadTexts: dnsServZoneName.setStatus('current')
if mibBuilder.loadTexts: dnsServZoneName.setDescription("DNS name of the zone described by this row of the table.\n            This is the owner name of the SOA RR that defines the\n            top of the zone. This is name is in uppercase:\n            characters 'a' through 'z' are mapped to 'A' through 'Z'\n            in order to make the lexical ordering useful.")
dnsServZoneClass = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 2), DnsClass())
if mibBuilder.loadTexts: dnsServZoneClass.setStatus('current')
if mibBuilder.loadTexts: dnsServZoneClass.setDescription('DNS class of the RRs in this zone.')
dnsServZoneLastReloadSuccess = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 3), DnsTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServZoneLastReloadSuccess.setStatus('current')
if mibBuilder.loadTexts: dnsServZoneLastReloadSuccess.setDescription('Elapsed time in seconds since last successful reload of\n            this zone.')
dnsServZoneLastReloadAttempt = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 4), DnsTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServZoneLastReloadAttempt.setStatus('current')
if mibBuilder.loadTexts: dnsServZoneLastReloadAttempt.setDescription('Elapsed time in seconds since last attempted reload of\n            this zone.')
dnsServZoneLastSourceAttempt = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServZoneLastSourceAttempt.setStatus('current')
if mibBuilder.loadTexts: dnsServZoneLastSourceAttempt.setDescription('IP address of host from which most recent zone transfer\n            of this zone was attempted.  This value should match the\n            value of dnsServZoneSourceSuccess if the attempt was\n            succcessful.  If zone transfer has not been attempted\n            within the memory of this name server, this value should\n            be 0.0.0.0.')
dnsServZoneStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dnsServZoneStatus.setStatus('current')
if mibBuilder.loadTexts: dnsServZoneStatus.setDescription('The status of the information represented in this row of\n            the table.')
dnsServZoneSerial = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServZoneSerial.setStatus('current')
if mibBuilder.loadTexts: dnsServZoneSerial.setDescription('Zone serial number (from the SOA RR) of the zone\n            represented by this row of the table.  If the zone has\n            not been successfully loaded within the memory of this\n            name server, the value of this variable is zero.')
dnsServZoneCurrent = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServZoneCurrent.setStatus('current')
if mibBuilder.loadTexts: dnsServZoneCurrent.setDescription("Whether the server's copy of the zone represented by\n            this row of the table is currently valid.  If the zone\n            has never been successfully loaded or has expired since\n            it was last succesfully loaded, this variable will have\n            the value false(2), otherwise this variable will have\n            the value true(1).")
dnsServZoneLastSourceSuccess = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServZoneLastSourceSuccess.setStatus('current')
if mibBuilder.loadTexts: dnsServZoneLastSourceSuccess.setDescription('IP address of host which was the source of the most\n            recent successful zone transfer for this zone.  If\n            unknown (e.g., zone has never been successfully\n            transfered) or irrelevant (e.g., zone was loaded from\n            stable storage), this value should be 0.0.0.0.')
dnsServZoneSrcTable = MibTable((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 2), )
if mibBuilder.loadTexts: dnsServZoneSrcTable.setStatus('current')
if mibBuilder.loadTexts: dnsServZoneSrcTable.setDescription('This table is a list of IP addresses from which the\n            server will attempt to load zone information using DNS\n            zone transfer operations.  A reload may occur due to SNMP\n            operations that create a row in dnsServZoneTable or a\n            SET to object dnsServZoneReload.  This table is only\n            used when the zone is loaded via zone transfer.')
dnsServZoneSrcEntry = MibTableRow((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 2, 1), ).setIndexNames((0, "DNS-SERVER-MIB", "dnsServZoneSrcName"), (0, "DNS-SERVER-MIB", "dnsServZoneSrcClass"), (0, "DNS-SERVER-MIB", "dnsServZoneSrcAddr"))
if mibBuilder.loadTexts: dnsServZoneSrcEntry.setStatus('current')
if mibBuilder.loadTexts: dnsServZoneSrcEntry.setDescription('An entry in the name server zone source table.')
dnsServZoneSrcName = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 2, 1, 1), DnsNameAsIndex())
if mibBuilder.loadTexts: dnsServZoneSrcName.setStatus('current')
if mibBuilder.loadTexts: dnsServZoneSrcName.setDescription('DNS name of the zone to which this entry applies.')
dnsServZoneSrcClass = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 2, 1, 2), DnsClass())
if mibBuilder.loadTexts: dnsServZoneSrcClass.setStatus('current')
if mibBuilder.loadTexts: dnsServZoneSrcClass.setDescription('DNS class of zone to which this entry applies.')
dnsServZoneSrcAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 2, 1, 3), IpAddress())
if mibBuilder.loadTexts: dnsServZoneSrcAddr.setStatus('current')
if mibBuilder.loadTexts: dnsServZoneSrcAddr.setDescription('IP address of name server host from which this zone\n            might be obtainable.')
dnsServZoneSrcStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dnsServZoneSrcStatus.setStatus('current')
if mibBuilder.loadTexts: dnsServZoneSrcStatus.setDescription('The status of the information represented in this row of\n            the table.')
dnsServMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 32, 1, 2))
dnsServConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 32, 1, 2, 1)).setObjects(("DNS-SERVER-MIB", "dnsServConfigImplementIdent"), ("DNS-SERVER-MIB", "dnsServConfigRecurs"), ("DNS-SERVER-MIB", "dnsServConfigUpTime"), ("DNS-SERVER-MIB", "dnsServConfigResetTime"), ("DNS-SERVER-MIB", "dnsServConfigReset"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dnsServConfigGroup = dnsServConfigGroup.setStatus('current')
if mibBuilder.loadTexts: dnsServConfigGroup.setDescription('A collection of objects providing basic configuration\n            control of a DNS name server.')
dnsServCounterGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 32, 1, 2, 2)).setObjects(("DNS-SERVER-MIB", "dnsServCounterAuthAns"), ("DNS-SERVER-MIB", "dnsServCounterAuthNoNames"), ("DNS-SERVER-MIB", "dnsServCounterAuthNoDataResps"), ("DNS-SERVER-MIB", "dnsServCounterNonAuthDatas"), ("DNS-SERVER-MIB", "dnsServCounterNonAuthNoDatas"), ("DNS-SERVER-MIB", "dnsServCounterReferrals"), ("DNS-SERVER-MIB", "dnsServCounterErrors"), ("DNS-SERVER-MIB", "dnsServCounterRelNames"), ("DNS-SERVER-MIB", "dnsServCounterReqRefusals"), ("DNS-SERVER-MIB", "dnsServCounterReqUnparses"), ("DNS-SERVER-MIB", "dnsServCounterOtherErrors"), ("DNS-SERVER-MIB", "dnsServCounterOpCode"), ("DNS-SERVER-MIB", "dnsServCounterQClass"), ("DNS-SERVER-MIB", "dnsServCounterQType"), ("DNS-SERVER-MIB", "dnsServCounterTransport"), ("DNS-SERVER-MIB", "dnsServCounterRequests"), ("DNS-SERVER-MIB", "dnsServCounterResponses"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dnsServCounterGroup = dnsServCounterGroup.setStatus('current')
if mibBuilder.loadTexts: dnsServCounterGroup.setDescription('A collection of objects providing basic instrumentation\n            of a DNS name server.')
dnsServOptCounterGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 32, 1, 2, 3)).setObjects(("DNS-SERVER-MIB", "dnsServOptCounterSelfAuthAns"), ("DNS-SERVER-MIB", "dnsServOptCounterSelfAuthNoNames"), ("DNS-SERVER-MIB", "dnsServOptCounterSelfAuthNoDataResps"), ("DNS-SERVER-MIB", "dnsServOptCounterSelfNonAuthDatas"), ("DNS-SERVER-MIB", "dnsServOptCounterSelfNonAuthNoDatas"), ("DNS-SERVER-MIB", "dnsServOptCounterSelfReferrals"), ("DNS-SERVER-MIB", "dnsServOptCounterSelfErrors"), ("DNS-SERVER-MIB", "dnsServOptCounterSelfRelNames"), ("DNS-SERVER-MIB", "dnsServOptCounterSelfReqRefusals"), ("DNS-SERVER-MIB", "dnsServOptCounterSelfReqUnparses"), ("DNS-SERVER-MIB", "dnsServOptCounterSelfOtherErrors"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsAuthAns"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsAuthNoNames"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsAuthNoDataResps"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsNonAuthDatas"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsNonAuthNoDatas"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsReferrals"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsErrors"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsRelNames"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsReqRefusals"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsReqUnparses"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsOtherErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dnsServOptCounterGroup = dnsServOptCounterGroup.setStatus('current')
if mibBuilder.loadTexts: dnsServOptCounterGroup.setDescription('A collection of objects providing extended\n            instrumentation of a DNS name server.')
dnsServZoneGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 32, 1, 2, 4)).setObjects(("DNS-SERVER-MIB", "dnsServZoneName"), ("DNS-SERVER-MIB", "dnsServZoneClass"), ("DNS-SERVER-MIB", "dnsServZoneLastReloadSuccess"), ("DNS-SERVER-MIB", "dnsServZoneLastReloadAttempt"), ("DNS-SERVER-MIB", "dnsServZoneLastSourceAttempt"), ("DNS-SERVER-MIB", "dnsServZoneLastSourceSuccess"), ("DNS-SERVER-MIB", "dnsServZoneStatus"), ("DNS-SERVER-MIB", "dnsServZoneSerial"), ("DNS-SERVER-MIB", "dnsServZoneCurrent"), ("DNS-SERVER-MIB", "dnsServZoneSrcName"), ("DNS-SERVER-MIB", "dnsServZoneSrcClass"), ("DNS-SERVER-MIB", "dnsServZoneSrcAddr"), ("DNS-SERVER-MIB", "dnsServZoneSrcStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dnsServZoneGroup = dnsServZoneGroup.setStatus('current')
if mibBuilder.loadTexts: dnsServZoneGroup.setDescription('A collection of objects providing configuration control\n            of a DNS name server which loads authoritative zones.')
dnsServMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 32, 1, 3))
dnsServMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 32, 1, 3, 1)).setObjects(("DNS-SERVER-MIB", "dnsServConfigGroup"), ("DNS-SERVER-MIB", "dnsServCounterGroup"), ("DNS-SERVER-MIB", "dnsServOptCounterGroup"), ("DNS-SERVER-MIB", "dnsServZoneGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dnsServMIBCompliance = dnsServMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: dnsServMIBCompliance.setDescription('The compliance statement for agents implementing the DNS\n            name server MIB extensions.')
mibBuilder.exportSymbols("DNS-SERVER-MIB", dnsServCounterEntry=dnsServCounterEntry, dnsServZoneTable=dnsServZoneTable, dns=dns, dnsServZone=dnsServZone, dnsServCounterReqRefusals=dnsServCounterReqRefusals, dnsServOptCounterSelfReqUnparses=dnsServOptCounterSelfReqUnparses, DnsTime=DnsTime, dnsServZoneStatus=dnsServZoneStatus, dnsServZoneSrcAddr=dnsServZoneSrcAddr, dnsServZoneSrcTable=dnsServZoneSrcTable, dnsServMIBCompliances=dnsServMIBCompliances, dnsServCounterTransport=dnsServCounterTransport, dnsServZoneSerial=dnsServZoneSerial, dnsServZoneEntry=dnsServZoneEntry, dnsServOptCounterFriendsAuthAns=dnsServOptCounterFriendsAuthAns, dnsServConfig=dnsServConfig, dnsServOptCounterSelfReferrals=dnsServOptCounterSelfReferrals, dnsServZoneSrcClass=dnsServZoneSrcClass, DnsClass=DnsClass, dnsServZoneClass=dnsServZoneClass, dnsServOptCounterSelfNonAuthDatas=dnsServOptCounterSelfNonAuthDatas, DnsRespCode=DnsRespCode, dnsServCounterOtherErrors=dnsServCounterOtherErrors, dnsServCounterOpCode=dnsServCounterOpCode, dnsServOptCounterFriendsAuthNoNames=dnsServOptCounterFriendsAuthNoNames, dnsServCounterNonAuthNoDatas=dnsServCounterNonAuthNoDatas, dnsServCounterGroup=dnsServCounterGroup, dnsServCounterQClass=dnsServCounterQClass, DnsName=DnsName, dnsServOptCounterSelfAuthAns=dnsServOptCounterSelfAuthAns, dnsServZoneSrcName=dnsServZoneSrcName, dnsServOptCounterSelfNonAuthNoDatas=dnsServOptCounterSelfNonAuthNoDatas, dnsServZoneGroup=dnsServZoneGroup, dnsServConfigReset=dnsServConfigReset, DnsOpCode=DnsOpCode, dnsServZoneSrcStatus=dnsServZoneSrcStatus, dnsServCounterRequests=dnsServCounterRequests, dnsServCounterAuthAns=dnsServCounterAuthAns, dnsServOptCounterSelfAuthNoNames=dnsServOptCounterSelfAuthNoNames, dnsServConfigUpTime=dnsServConfigUpTime, dnsServConfigImplementIdent=dnsServConfigImplementIdent, dnsServCounterResponses=dnsServCounterResponses, dnsServOptCounterFriendsReqUnparses=dnsServOptCounterFriendsReqUnparses, dnsServOptCounterFriendsReferrals=dnsServOptCounterFriendsReferrals, DnsQType=DnsQType, dnsServOptCounterGroup=dnsServOptCounterGroup, dnsServMIBObjects=dnsServMIBObjects, PYSNMP_MODULE_ID=dnsServMIB, dnsServOptCounterFriendsNonAuthNoDatas=dnsServOptCounterFriendsNonAuthNoDatas, dnsServZoneSrcEntry=dnsServZoneSrcEntry, dnsServCounterReferrals=dnsServCounterReferrals, dnsServOptCounterFriendsErrors=dnsServOptCounterFriendsErrors, dnsServZoneLastReloadSuccess=dnsServZoneLastReloadSuccess, dnsServOptCounterFriendsRelNames=dnsServOptCounterFriendsRelNames, dnsServCounterAuthNoDataResps=dnsServCounterAuthNoDataResps, dnsServCounterAuthNoNames=dnsServCounterAuthNoNames, dnsServMIB=dnsServMIB, dnsServCounter=dnsServCounter, dnsServOptCounterSelfRelNames=dnsServOptCounterSelfRelNames, dnsServMIBGroups=dnsServMIBGroups, dnsServZoneLastReloadAttempt=dnsServZoneLastReloadAttempt, dnsServOptCounterFriendsOtherErrors=dnsServOptCounterFriendsOtherErrors, dnsServCounterRelNames=dnsServCounterRelNames, dnsServOptCounterSelfOtherErrors=dnsServOptCounterSelfOtherErrors, dnsServConfigGroup=dnsServConfigGroup, dnsServZoneLastSourceAttempt=dnsServZoneLastSourceAttempt, dnsServCounterTable=dnsServCounterTable, dnsServOptCounterFriendsNonAuthDatas=dnsServOptCounterFriendsNonAuthDatas, dnsServCounterReqUnparses=dnsServCounterReqUnparses, DnsType=DnsType, dnsServOptCounterSelfAuthNoDataResps=dnsServOptCounterSelfAuthNoDataResps, dnsServOptCounterFriendsAuthNoDataResps=dnsServOptCounterFriendsAuthNoDataResps, dnsServZoneCurrent=dnsServZoneCurrent, dnsServOptCounter=dnsServOptCounter, dnsServConfigResetTime=dnsServConfigResetTime, dnsServCounterErrors=dnsServCounterErrors, DnsQClass=DnsQClass, dnsServOptCounterSelfReqRefusals=dnsServOptCounterSelfReqRefusals, dnsServCounterNonAuthDatas=dnsServCounterNonAuthDatas, dnsServConfigRecurs=dnsServConfigRecurs, dnsServOptCounterSelfErrors=dnsServOptCounterSelfErrors, dnsServCounterQType=dnsServCounterQType, dnsServZoneLastSourceSuccess=dnsServZoneLastSourceSuccess, dnsServOptCounterFriendsReqRefusals=dnsServOptCounterFriendsReqRefusals, dnsServMIBCompliance=dnsServMIBCompliance, dnsServZoneName=dnsServZoneName, DnsNameAsIndex=DnsNameAsIndex)
