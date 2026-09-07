#
# PySNMP MIB module CISCO-NTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-NTP-MIB
# Source digest sha256:f0a1321b78d56a9c29a8f2021523b264e210224a56ea4e7af14075e5f62351ee
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
ciscoNtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 168))
ciscoNtpMIB.setRevisions(('2006-07-31 00:00', '2004-07-23 00:00', '2003-07-29 00:00', '2003-07-07 00:00', '2002-02-20 00:00', '2000-06-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoNtpMIB.setRevisionsDescriptions(('Added ciscoNtpSysExtGroup and ciscoNtpSrvNotifGroup groups\n             to support monitoring of NTP server status.\n             ciscoNtpMIBComplianceRev3 is deprecated and replaced\n             by ciscoNtpMIBComplianceRev4.', 'Added cntpPeersPeerName and cntpPeersPeerType\n            objects to cntpPeerVarTable.', 'Added cntpPeersPrefPeer object to\n            cntpPeersVarTable.', 'ciscoNtpPeersGroup is deprecated by\n            ciscoNtpPeersGroupRev1.\n            ciscoNtpMIBCompliance is deprecated by\n            ciscoNtpMIBComplianceRev1.', 'cntpPeersUpdateTime is deprecated by\n            cntpPeersUpdateTimeRev1.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoNtpMIB.setLastUpdated('2006-07-31 00:00')
if mibBuilder.loadTexts: ciscoNtpMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoNtpMIB.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W. Tasman Drive\n            San Jose, CA 95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoNtpMIB.setDescription('This MIB module defines a MIB which provides\n            mechanisms to monitor an NTP server.\n\n            The MIB is derived from the Technical Report\n            #Management of the NTP with SNMP# TR No. 98-09\n            authored by A.S. Sethi and Dave Mills in the\n            University of Delaware.\n\n            Below is a brief overview of NTP system architecture\n            and implementation model. This will help understand\n            the objects defined below and their relationships.\n\n            NTP Intro:\n            The Network Time Protocol (NTP) Version 3, is used to\n            synchronize timekeeping among a set of distributed\n            time servers and clients.  The service model is based\n            on a returnable-time design which depends only on\n            measured clock offsets, but does not require reliable\n            message delivery.  The synchronization subnet uses a\n            self-organizing, hierarchical master-slave\n            configuration, with synchronization paths determined\n            by a minimum-weight spanning tree.  While multiple\n            masters (primary servers) may exist, there is no\n            requirement for an election protocol.\n\n            System Archiecture:\n            In the NTP model a number of primary reference\n            sources, synchronized by wire or radio to national\n            standards, are connected to widely accessible\n            resources, such as backbone gateways, and operated as\n            primary time servers.  The purpose of NTP is to convey\n            timekeeping information from these servers to other\n            time servers via the Internet and also to cross-check\n            clocks and mitigate errors due to equipment or\n            propagation failures.  Some number of local-net hosts\n            or gateways, acting as secondary time servers, run NTP\n            with one or more of the primary servers.  In order to\n            reduce the protocol overhead, the secondary servers\n            distribute time via NTP to the remaining local-net\n            hosts.  In the interest of reliability, selected hosts\n            can be equipped with less accurate but less expensive\n            radio clocks and used for backup in case of failure of\n            the primary and/or secondary servers or communication\n            paths between them.\n\n            NTP is designed to produce three products: clock\n            offset, round-trip delay and dispersion, all of which\n            are relative to a selected reference clock.  Clock\n            offset represents the amount to adjust the local clock\n            to bring it into correspondence with the reference\n            clock.  Roundtrip delay provides the capability to\n            launch a message to arrive at the reference clock at a\n            specified time.  Dispersion represents the maximum\n            error of the local clock relative to the reference\n            clock.  Since most host time servers will synchronize\n            via another peer time server, there are two components\n            in each of these three products, those determined by\n            the peer relative to the primary reference source of\n            standard time and those measured by the host relative\n            to the peer.  Each of these components are maintained\n            separately in the protocol in order to facilitate\n            error control and management of the subnet itself.  \n            They provide not only precision measurements of offset\n            and delay, but also definitive maximum error bounds,\n            so that the user interface can determine not only the\n            time, but the quality of the time as well.\n\n            Implementation Model:\n            In what may be the most common client/server model a\n            client sends an NTP message to one or more servers and\n            processes the replies as received.  The server\n            interchanges addresses and ports, overwrites certain\n            fields in the message, recalculates the checksum and\n            returns the message immediately.  Information included\n            in the NTP message allows the client to determine the\n            server time with respect to local time and adjust the\n            local clock accordingly.  In addition, the message\n            includes information to calculate the expected\n            timekeeping accuracy and reliability, as well as\n            select the best from possibly several servers.\n\n            While the client/server model may suffice for use on\n            local nets involving a public server and perhaps many\n            workstation clients, the full generality of NTP\n            requires distributed participation of a number of\n            client/servers or peers arranged in a dynamically\n            reconfigurable, hierarchically distributed\n            configuration.  It also requires sophisticated\n            algorithms for association management, data\n            manipulation and local-clock control.\n\n            Glossary:\n            1. Host: Refers to an instantiation of the NTP\n                    protocol on a local processor.\n            2. Peer: Refers to an instantiation of the NTP\n                    protocol on a remote processor connected by\n                    a network path from the local host.')
ciscoNtpMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 168, 0))
ciscoNtpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 168, 1))
ciscoNtpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 168, 2))
cntpSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1))
cntpPeers = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2))
cntpFilter = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 3))
class NTPTimeStamp(TextualConvention, OctetString):
    reference = "D.L. Mills, 'Network Time Protocol (Version 3)',\n                RFC-1305, March 1992, Section 3.1"
    description = 'NTP timestamps are represented as a 64-bit\n            unsigned fixed-point number, in seconds relative to\n            00:00 on 1 January 1900.  The integer part is in the\n            first 32 bits and the fraction part is in the last\n            32 bits.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class NTPLeapIndicator(TextualConvention, Integer32):
    reference = "D.L. Mills, 'Network Time Protocol(Version 3)',\n                RFC-1305, March 1992, Section 3.2.1"
    description = 'This is a two-bit code warning of an impending leap\n            second to be inserted in the NTP timescale.  The bits\n            are set before 23:59 on the day of insertion and reset\n            after 00:00 on the following day.  This causes the\n            number of seconds (rollover interval) in the day of\n            insertion to be increased or decreased by one.  The two\n            bits are coded as below,\n            00, no warning\n            01, last minute has 61 seconds\n            10, last minute has 59 seconds\n            11, alarm condition (clock not synchronized)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("noWarning", 0), ("addSecond", 1), ("subtractSecond", 2), ("alarm", 3))

class NTPSignedTimeValue(TextualConvention, OctetString):
    reference = "D.L. Mills, 'Network Time Protocol (Version 3)',\n                RFC-1305, March 1992, Sections 2,  3.2.1"
    description = 'The time in seconds that could represent signed\n            quantities like time delay with respect to some\n            source.  This textual-convention is specific to Cisco\n            implementation of NTP where 32-bit integers are used\n            for such quantities.  The signed integer part is in\n            the first 16 bits and the fraction part is in the\n            last 16 bits.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class NTPUnsignedTimeValue(TextualConvention, OctetString):
    reference = "D.L. Mills, 'Network Time Protocol (Version 3)',\n                RFC-1305, March 1992, Sections 2, 3.2.1"
    description = 'The time in seconds that could represent unsigned\n            quantities like maximum error of the local clock\n            with respect to some source.  This textual-convention\n            is specific to Cisco implementation of NTP where\n            32-bit integers are used for such quantities.  The\n            unsigned integer part is in the first 16 bits and the\n            fraction part is in the last 16 bits.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class NTPStratum(TextualConvention, Integer32):
    reference = "D.L. Mills, 'Network Time Protocol (Version 3)',\n                RFC-1305, March 1992, Section 2.2"
    description = 'Indicates the stratum of the clock.  The stratum\n            defines the accuracy of a time server.  Higher the\n            stratum, lower the accuracy.\n            0, unspecified\n            1, primary reference (e.g., calibrated atomic clock,\n               radio clock)\n            2-255, secondary reference (via NTP)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class NTPRefId(TextualConvention, OctetString):
    reference = "D.L. Mills, Network Time Protocol (Version 3)',\n                RFC-1305, March 1992, Section 3.2.1"
    description = 'The reference clock identifier.  In the case of\n            stratum 0 (unspecified) or stratum 1 (primary\n            reference source), this is a four-octet,\n            left-justified, zero-padded ASCII string as defined\n            in RFC-1305.  In the case of stratum 2 and greater\n            (secondary reference) this is the four-octet Internet\n            address of the peer selected for synchronization.\n\n            Some examples of stratum 0 identifiers are,\n            DCN, DCN routing protocol\n            NIST, NIST public modem\n            TSP, TSP time protocol\n            DTS, Digital Time Service\n\n            Some examples of stratum 1 identifiers are,\n            ATOM, Atomic clock (calibrated)\n            VLF, VLF radio (OMEGA,, etc.)\n            LORC, LORAN-C radionavigation\n            GOES, GOES UHF environment satellite\n            GPS, GPS UHF satellite positioning'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class NTPPollInterval(TextualConvention, Integer32):
    description = 'The minimum interval between transmitted NTP\n            messages, in seconds as a power of two.  For\n            instance, a value of six indicates a minimum\n            interval of 64 seconds.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-20, 20)

class NTPAssocIdentifier(TextualConvention, Integer32):
    description = 'The association identifier of the peer.  Every peer\n            with which an NTP server is associated with is\n            identified by an association identifier.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

cntpSysLeap = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 1), NTPLeapIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cntpSysLeap.setStatus('current')
if mibBuilder.loadTexts: cntpSysLeap.setDescription('Two-bit code warning of an impending leap second to\n            be inserted in the NTP timescale. This object can be\n            set only when the cntpSysStratum has a value of 1.')
cntpSysStratum = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 2), NTPStratum()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cntpSysStratum.setStatus('current')
if mibBuilder.loadTexts: cntpSysStratum.setDescription('The stratum of the local clock. If the value is set\n            to 1, i.e., this is a primary reference, then the\n            Primary-Clock procedure described in Section 3.4.6,\n            in RFC-1305 is invoked.')
cntpSysPrecision = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-20, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpSysPrecision.setStatus('current')
if mibBuilder.loadTexts: cntpSysPrecision.setDescription('Signed integer indicating the precision\n            of the system clock, in seconds to the nearest\n            power of two.  The value must be rounded to the\n            next larger power of two; for instance, a 50-Hz\n            (20 ms) or 60-Hz (16.67 ms) power-frequency clock\n            would be assigned the value -5 (31.25 ms), while a\n            1000-Hz (1 ms) crystal-controlled clock would be\n            assigned the value -9 (1.95 ms).')
cntpSysRootDelay = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 4), NTPSignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpSysRootDelay.setReference("D.L. Mills, 'Network Time Protocol (Version 3)',\n                RFC-1305, March 1992, Sections 2.2, 3.2.1")
if mibBuilder.loadTexts: cntpSysRootDelay.setStatus('current')
if mibBuilder.loadTexts: cntpSysRootDelay.setDescription('A signed fixed-point number indicating the total\n            round-trip delay in seconds, to the primary reference\n            source at the root of the synchronization subnet.')
cntpSysRootDispersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 5), NTPUnsignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpSysRootDispersion.setReference("D.L. Mills, 'Network Time Protocol (Version 3)',\n                RFC-1305, March 1992, Sections 2, 2.2, 3.2.1")
if mibBuilder.loadTexts: cntpSysRootDispersion.setStatus('current')
if mibBuilder.loadTexts: cntpSysRootDispersion.setDescription('The maximum error in seconds, relative to the\n            primary reference source at the root of the\n            synchronization subnet.  Only positive values greater\n            than zero are possible.')
cntpSysRefId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 6), NTPRefId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpSysRefId.setStatus('current')
if mibBuilder.loadTexts: cntpSysRefId.setDescription('The reference identifier of the local clock.')
cntpSysRefTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 7), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpSysRefTime.setStatus('current')
if mibBuilder.loadTexts: cntpSysRefTime.setDescription('The local time when the local clock was last\n            updated.  If the local clock has never been\n            synchronized, the value is zero.')
cntpSysPoll = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 8), NTPPollInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpSysPoll.setStatus('current')
if mibBuilder.loadTexts: cntpSysPoll.setDescription('The interval at which the NTP server polls other NTP\n            servers to synchronize its clock.')
cntpSysPeer = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 9), NTPAssocIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpSysPeer.setStatus('current')
if mibBuilder.loadTexts: cntpSysPeer.setDescription('The current synchronization source.  This will\n            contain the unique association identifier\n            cntpPeersAssocId of the corresponding peer entry in\n            the cntpPeersVarTable of the peer acting as the\n            synchronization source.  If there is no peer, the\n            value will be 0.')
cntpSysClock = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 10), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpSysClock.setStatus('current')
if mibBuilder.loadTexts: cntpSysClock.setDescription('The current local time.  Local time is derived from\n            the hardware clock of the particular machine and\n            increments at intervals depending on the design used.')
cntpSysSrvStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 1), ("notRunning", 2), ("notSynchronized", 3), ("syncToLocal", 4), ("syncToRefclock", 5), ("syncToRemoteServer", 6))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpSysSrvStatus.setStatus('current')
if mibBuilder.loadTexts: cntpSysSrvStatus.setDescription('Current state of the NTP server with values coded as follows:\n            1: server status is unknown\n            2: server is not running\n            3: server is not synchronized to any time source\n            4: server is synchronized to its own local clock\n            5: server is synchronized to a local hardware refclock (e.g. GPS)\n            6: server is synchronized to a remote NTP server')
cntpPeersVarTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cntpPeersVarTable.setStatus('current')
if mibBuilder.loadTexts: cntpPeersVarTable.setDescription('This table provides information on the peers with\n            which the local NTP server has associations.  The\n            peers are also NTP servers but running on different\n            hosts.')
cntpPeersVarEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-NTP-MIB", "cntpPeersAssocId"))
if mibBuilder.loadTexts: cntpPeersVarEntry.setStatus('current')
if mibBuilder.loadTexts: cntpPeersVarEntry.setDescription("Each peers' entry provides NTP information retrieved\n            from a particular peer NTP server.  Each peer is\n            identified by a unique association identifier.\n\n            Entries are automatically created when the user\n            configures the NTP server to be associated with remote\n            peers.  Similarly entries are deleted when the user\n            removes the peer association from the NTP server.\n\n            Entries can also be created by the management station\n            by setting values for the following objects:\n            cntpPeersPeerAddress or cntpPeersPeerName, \n            cntpPeersHostAddress and\n            cntpPeersMode and making the cntpPeersEntryStatus as\n            active(1).  At the least, the management station has\n            to set a value for cntpPeersPeerAddress or\n            cntpPeersPeerName to make the row active.")
cntpPeersAssocId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 1), NTPAssocIdentifier()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cntpPeersAssocId.setStatus('current')
if mibBuilder.loadTexts: cntpPeersAssocId.setDescription('An integer value greater than 0 that uniquely\n            identifies a peer with which the local NTP server\n            is associated.')
cntpPeersConfigured = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersConfigured.setStatus('current')
if mibBuilder.loadTexts: cntpPeersConfigured.setDescription('This is a bit indicating that the association\n            was created from configuration information and\n            should not be de-associated even if the peer\n            becomes unreachable.')
cntpPeersPeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cntpPeersPeerAddress.setStatus('current')
if mibBuilder.loadTexts: cntpPeersPeerAddress.setDescription('The IP address of the peer.  When creating a new\n            association, a value should be set either for this\n            object or the corresponding instance of \n            cntpPeersPeerName, before the row is made active.')
cntpPeersPeerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersPeerPort.setStatus('current')
if mibBuilder.loadTexts: cntpPeersPeerPort.setDescription('The UDP port number on which the peer receives NTP\n            messages.')
cntpPeersHostAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cntpPeersHostAddress.setStatus('current')
if mibBuilder.loadTexts: cntpPeersHostAddress.setDescription('The IP address of the local host.  Multi-homing can\n            be supported using this object.')
cntpPeersHostPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersHostPort.setStatus('current')
if mibBuilder.loadTexts: cntpPeersHostPort.setDescription('The UDP port number on which the local host receives\n            NTP messages.')
cntpPeersLeap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 7), NTPLeapIndicator()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersLeap.setStatus('current')
if mibBuilder.loadTexts: cntpPeersLeap.setDescription('Two-bit code warning of an impending leap\n            second to be inserted in the NTP timescale of\n            the peer.')
cntpPeersMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unspecified", 0), ("symmetricActive", 1), ("symmetricPassive", 2), ("client", 3), ("server", 4), ("broadcast", 5), ("reservedControl", 6), ("reservedPrivate", 7)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cntpPeersMode.setReference("D.L. Mills, 'Network Time Protocol (Version 3)',\n                RFC-1305, March 1992, Section 3.3")
if mibBuilder.loadTexts: cntpPeersMode.setStatus('current')
if mibBuilder.loadTexts: cntpPeersMode.setDescription('The association mode of the NTP server, with values\n            coded as follows,\n            0, unspecified\n            1, symmetric active - A host operating in this mode\n                    sends periodic messages regardless of the\n                    reachability state or stratum of its peer.  By\n                    operating in this mode the host announces its\n                    willingness to synchronize and be synchronized\n                    by the peer\n            2, symmetric passive - This type of association is\n                    ordinarily created upon arrival of a message\n                    from a peer operating in the symmetric active\n                    mode and persists only as long as the peer is\n                    reachable and operating at a stratum level\n                    less than or equal to the host; otherwise, the\n                    association is dissolved.  However, the\n                    association will always persist until at least\n                    one message has been sent in reply.  By\n                    operating in this mode the host announces its\n                    willingness to synchronize and be synchronized\n                    by the peer\n            3, client -  A host operating in this mode sends\n                    periodic messages regardless of the\n                    reachability state or stratum of its peer.  By\n                    operating in this mode the host, usually a LAN\n                    workstation, announces its willingness to be\n                    synchronized by, but not to synchronize the peer\n            4, server - This type of association is ordinarily\n                    created upon arrival of a client request message\n                    and exists only in order to reply to that\n                    request, after which the association is\n                    dissolved.  By operating in this mode the host,\n                    usually a LAN time server, announces its\n                    willingness to synchronize, but not to be\n                    synchronized by the peer\n            5, broadcast - A host operating in this mode sends\n                    periodic messages regardless of the\n                    reachability state or stratum of the peers.\n                    By operating in this mode the host, usually a\n                    LAN time server operating on a high-speed\n                    broadcast medium, announces its willingness to\n                    synchronize all of the peers, but not to be\n                    synchronized by any of them\n            6, reserved for NTP control messages\n            7, reserved for private use.\n\n            When creating a new peer association, if no value\n            is specified for this object, it defaults to\n            symmetricActive(1).')
cntpPeersStratum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 9), NTPStratum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersStratum.setStatus('current')
if mibBuilder.loadTexts: cntpPeersStratum.setDescription('The stratum of the peer clock.')
cntpPeersPeerPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 10), NTPPollInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersPeerPoll.setStatus('current')
if mibBuilder.loadTexts: cntpPeersPeerPoll.setDescription('The interval at which the peer polls the local host.')
cntpPeersHostPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 11), NTPPollInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersHostPoll.setStatus('current')
if mibBuilder.loadTexts: cntpPeersHostPoll.setDescription('The interval at which the local host polls the peer.')
cntpPeersPrecision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-20, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersPrecision.setStatus('current')
if mibBuilder.loadTexts: cntpPeersPrecision.setDescription('Signed integer indicating the precision of the peer\n            clock, in seconds to the nearest power of two.  The\n            value must be rounded to the next larger power of\n            two; for instance, a 50-Hz (20 ms) or 60-Hz\n            (16.67 ms) power-frequency clock would be assigned\n            the value -5 (31.25 ms), while a 1000-Hz (1 ms)\n            crystal-controlled clock would be assigned the value\n            -9 (1.95 ms).')
cntpPeersRootDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 13), NTPSignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersRootDelay.setStatus('current')
if mibBuilder.loadTexts: cntpPeersRootDelay.setDescription('A signed fixed-point number indicating the total\n            round-trip delay in seconds, from the peer to the\n            primary reference source at the root of the\n            synchronization subnet.')
cntpPeersRootDispersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 14), NTPUnsignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersRootDispersion.setStatus('current')
if mibBuilder.loadTexts: cntpPeersRootDispersion.setDescription('The maximum error in seconds, of the peer clock\n            relative to the primary reference source at the root\n            of the synchronization subnet.  Only positive values\n            greater than zero are possible.')
cntpPeersRefId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 15), NTPRefId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersRefId.setStatus('current')
if mibBuilder.loadTexts: cntpPeersRefId.setDescription('The reference identifier of the peer.')
cntpPeersRefTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 16), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersRefTime.setStatus('current')
if mibBuilder.loadTexts: cntpPeersRefTime.setDescription('The local time at the peer when its clock was last\n            updated.  If the peer clock has never been\n            synchronized, the value is zero.')
cntpPeersOrgTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 17), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersOrgTime.setStatus('current')
if mibBuilder.loadTexts: cntpPeersOrgTime.setDescription('The local time at the peer, when its latest\n            NTP message was sent.  If the peer becomes unreachable\n            the value is set to zero.')
cntpPeersReceiveTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 18), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersReceiveTime.setStatus('current')
if mibBuilder.loadTexts: cntpPeersReceiveTime.setDescription('The local time, when the latest NTP message from\n            the peer arrived.  If the peer becomes unreachable\n            the value is set to zero.')
cntpPeersTransmitTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 19), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersTransmitTime.setStatus('current')
if mibBuilder.loadTexts: cntpPeersTransmitTime.setDescription('The local time at which the NTP message departed the\n            sender.')
cntpPeersUpdateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersUpdateTime.setStatus('deprecated')
if mibBuilder.loadTexts: cntpPeersUpdateTime.setDescription('The local time, when the most recent NTP message was\n            received from the peer that was used to calculate the\n            skew dispersion.  This represents only the 32-bit\n            integer part of the NTPTimestamp.')
cntpPeersReach = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersReach.setReference("D.L. Mills, 'Network Time Protocol (Version 3)',\n                RFC-1305, March 1992, Section 3.2.3")
if mibBuilder.loadTexts: cntpPeersReach.setStatus('current')
if mibBuilder.loadTexts: cntpPeersReach.setDescription('A shift register of used to determine the\n            reachability status of the peer, with bits entering\n            from the least significant (rightmost) end.  A peer is\n            considered reachable if at least one bit in this\n            register is set to one i.e, if the value of this\n            object is non-zero.\n            The data in the shift register would be populated by\n            the NTP protocol procedures.')
cntpPeersTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersTimer.setReference("D.L. Mills, 'Network Time Protocol (Version 3)',\n                RFC-1305, March 1992, Section 3.2.3")
if mibBuilder.loadTexts: cntpPeersTimer.setStatus('current')
if mibBuilder.loadTexts: cntpPeersTimer.setDescription('The interval in seconds, between transmitted NTP\n            messages from the local host to the peer.')
cntpPeersOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 23), NTPSignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersOffset.setReference("D.L. Mills, 'Network Time Protocol (Version 3)',\n                RFC-1305, March 1992, Section 3.2.5")
if mibBuilder.loadTexts: cntpPeersOffset.setStatus('current')
if mibBuilder.loadTexts: cntpPeersOffset.setDescription('The estimated offset of the peer clock relative to\n            the local clock, in seconds.  The host determines the\n            value of this object using the NTP clock-filter\n            algorithm.')
cntpPeersDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 24), NTPSignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersDelay.setReference("D.L. Mills, 'Network Time Protocol (Version 3)',\n                RFC-1305, March 1992, Section 3.2.5")
if mibBuilder.loadTexts: cntpPeersDelay.setStatus('current')
if mibBuilder.loadTexts: cntpPeersDelay.setDescription('The estimated round-trip delay of the peer clock\n            relative to the local clock over the network path\n            between them, in seconds.  The host determines the\n            value of this object using the NTP clock-filter\n            algorithm.')
cntpPeersDispersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 25), NTPUnsignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersDispersion.setReference("D.L. Mills, 'Network Time Protocol (Version 3)',\n                RFC-1305, March 1992, Section 3.2.5")
if mibBuilder.loadTexts: cntpPeersDispersion.setStatus('current')
if mibBuilder.loadTexts: cntpPeersDispersion.setDescription('The estimated maximum error of the peer clock\n            relative to the local clock over the network path\n            between them, in seconds.  The host determines the\n            value of this object using the NTP clock-filter\n            algorithm.')
cntpPeersFilterValidEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 26), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersFilterValidEntries.setStatus('current')
if mibBuilder.loadTexts: cntpPeersFilterValidEntries.setDescription('The number of valid entries for a peer in the\n            Filter Register Table. Since, the Filter Register\n            Table is optional, this object will have a value 0\n            if the Filter Register Table is not implemented.')
cntpPeersEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 27), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cntpPeersEntryStatus.setStatus('current')
if mibBuilder.loadTexts: cntpPeersEntryStatus.setDescription('The status object for this row. When a management\n            station is creating a new row, it should set the\n            value for cntpPeersPeerAddress at least, before the\n            row can be made active(1).')
cntpPeersUpdateTimeRev1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 28), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersUpdateTimeRev1.setStatus('current')
if mibBuilder.loadTexts: cntpPeersUpdateTimeRev1.setDescription('The local time, when the most recent NTP message was\n            received from the peer that was used to calculate the\n            skew dispersion.  This represents only the 32-bit\n            integer part of the NTPTimestamp.')
cntpPeersPrefPeer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 29), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cntpPeersPrefPeer.setStatus('current')
if mibBuilder.loadTexts: cntpPeersPrefPeer.setDescription("This object specifies whether this peer is the\n            preferred one over the others. By default, when\n            the value of this object is 'false', NTP chooses \n            the peer with which to synchronize the time on \n            the local system. If this object is set\n            to 'true', NTP will choose the corresponding\n            peer to synchronize the time with. If multiple\n            entries have this object set to 'true', NTP will\n            choose the first one to be set. This object is\n            a means to override the selection of the peer by\n            NTP.")
cntpPeersPeerType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 30), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cntpPeersPeerType.setStatus('current')
if mibBuilder.loadTexts: cntpPeersPeerType.setDescription('Represents the type of the corresponding instance\n            of cntpPeersPeerName object.')
cntpPeersPeerName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 31), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cntpPeersPeerName.setStatus('current')
if mibBuilder.loadTexts: cntpPeersPeerName.setDescription('The address of the peer. When creating a new\n            association, a value must be set for either this\n            object or the corresponding instance of\n            cntpPeersPeerAddress object, before the row\n            is made active.')
cntpFilterRegisterTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 3, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cntpFilterRegisterTable.setReference("D.L. Mills, 'Network Time Protocol (Version 3)',\n                RFC-1305, March 1992, Section 3.2.5")
if mibBuilder.loadTexts: cntpFilterRegisterTable.setStatus('current')
if mibBuilder.loadTexts: cntpFilterRegisterTable.setDescription('The following table contains NTP state variables\n            used by the NTP clock filter and selection algorithms.\n            This table depicts a shift register.  Each stage in\n            the shift register is a 3-tuple consisting of the\n            measured clock offset, measured clock delay and\n            measured clock dispersion associated with a single\n            observation.\n\n            An important factor affecting the accuracy and\n            reliability of time distribution is the complex of\n            algorithms used to reduce the effect of statistical\n            errors and falsetickers due to failure of various\n            subnet components, reference sources or propagation\n            media.  The NTP clock-filter and selection algorithms\n            are designed to do exactly this.  The objects in the\n            filter register table below are used by these\n            algorthims to minimize the error in the calculated\n            time.')
cntpFilterRegisterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 3, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-NTP-MIB", "cntpPeersAssocId"), (0, "CISCO-NTP-MIB", "cntpFilterIndex"))
if mibBuilder.loadTexts: cntpFilterRegisterEntry.setStatus('current')
if mibBuilder.loadTexts: cntpFilterRegisterEntry.setDescription('Each entry corresponds to one stage of the shift\n            register, i.e., one reading of the variables clock\n            delay, clock offset and clock dispersion.\n\n            Entries are automatically created whenever a peer is\n            configured and deleted when the peer is removed.')
cntpFilterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cntpFilterIndex.setStatus('current')
if mibBuilder.loadTexts: cntpFilterIndex.setDescription('An integer value in the specified range that is used\n            to index into the table.  The size of the table is\n            fixed at 8.  Each entry identifies a particular\n            reading of the clock filter variables in the shift\n            register.\n\n            Entries are added starting at index 1.  The index\n            wraps back to 1 when it reaches 8.  When the index\n            wraps back, the new entries will overwrite the old\n            entries effectively deleting the old entry.')
cntpFilterPeersOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 3, 2, 1, 2), NTPSignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpFilterPeersOffset.setStatus('current')
if mibBuilder.loadTexts: cntpFilterPeersOffset.setDescription('The offset of the peer clock relative to the\n            local clock in seconds.')
cntpFilterPeersDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 3, 2, 1, 3), NTPSignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpFilterPeersDelay.setStatus('current')
if mibBuilder.loadTexts: cntpFilterPeersDelay.setDescription('Round-trip delay of the peer clock relative to the\n            local clock over the network path between them, in\n            seconds.  This variable can take on both positive and\n            negative values, depending on clock precision and\n            skew-error accumulation.')
cntpFilterPeersDispersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 3, 2, 1, 4), NTPUnsignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpFilterPeersDispersion.setStatus('current')
if mibBuilder.loadTexts: cntpFilterPeersDispersion.setDescription('The maximum error of the peer clock relative to the\n            local clock over the network path between them, in\n            seconds.  Only positive values greater than zero are\n            possible.')
ciscoNtpSrvStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 168, 0, 1)).setObjects(("CISCO-NTP-MIB", "cntpSysSrvStatus"))
if mibBuilder.loadTexts: ciscoNtpSrvStatusChange.setStatus('current')
if mibBuilder.loadTexts: ciscoNtpSrvStatusChange.setDescription('This notification is generated whenever the value of\n            cntpSysSrvStatus changes.')
ciscoNtpHighPriorityConnFailure = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 168, 0, 2)).setObjects(("CISCO-NTP-MIB", "cntpPeersPeerAddress"))
if mibBuilder.loadTexts: ciscoNtpHighPriorityConnFailure.setStatus('current')
if mibBuilder.loadTexts: ciscoNtpHighPriorityConnFailure.setDescription('A failure to connect with an high priority NTP server\n            (e.g. a server at the lowest stratum) is detected.')
ciscoNtpHighPriorityConnRestore = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 168, 0, 3)).setObjects(("CISCO-NTP-MIB", "cntpPeersPeerAddress"))
if mibBuilder.loadTexts: ciscoNtpHighPriorityConnRestore.setStatus('current')
if mibBuilder.loadTexts: ciscoNtpHighPriorityConnRestore.setDescription('A connection with an high priority NTP server\n            (e.g. a server at the lowest stratum) is restored.')
ciscoNtpGeneralConnFailure = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 168, 0, 4))
if mibBuilder.loadTexts: ciscoNtpGeneralConnFailure.setStatus('current')
if mibBuilder.loadTexts: ciscoNtpGeneralConnFailure.setDescription('This trap is sent when the device loses connectivity \n            to all NTP servers.')
ciscoNtpGeneralConnRestore = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 168, 0, 5)).setObjects(("CISCO-NTP-MIB", "cntpPeersPeerAddress"))
if mibBuilder.loadTexts: ciscoNtpGeneralConnRestore.setStatus('current')
if mibBuilder.loadTexts: ciscoNtpGeneralConnRestore.setDescription('This trap is sent when the connection with at least \n            one NTP server has been restored\n            (e.g. after a ciscoNtpGeneralConnFailure).')
ciscoNtpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 1))
ciscoNtpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2))
ciscoNtpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 1, 1)).setObjects(("CISCO-NTP-MIB", "ciscoNtpSysGroup"), ("CISCO-NTP-MIB", "ciscoNtpPeersGroup"), ("CISCO-NTP-MIB", "ciscoNtpFilterGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpMIBCompliance = ciscoNtpMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoNtpMIBCompliance.setDescription('The compliance statement for Cisco agents which\n            implement the Cisco NTP MIB.')
ciscoNtpMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 1, 2)).setObjects(("CISCO-NTP-MIB", "ciscoNtpSysGroup"), ("CISCO-NTP-MIB", "ciscoNtpPeersGroupRev1"), ("CISCO-NTP-MIB", "ciscoNtpFilterGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpMIBComplianceRev1 = ciscoNtpMIBComplianceRev1.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoNtpMIBComplianceRev1.setDescription('The compliance statement for Cisco agents which\n            implement the Cisco NTP MIB.')
ciscoNtpMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 1, 3)).setObjects(("CISCO-NTP-MIB", "ciscoNtpSysGroup"), ("CISCO-NTP-MIB", "ciscoNtpPeersGroupRev1"), ("CISCO-NTP-MIB", "ciscoNtpFilterGroup"), ("CISCO-NTP-MIB", "ciscoNtpPeerExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpMIBComplianceRev2 = ciscoNtpMIBComplianceRev2.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoNtpMIBComplianceRev2.setDescription('The compliance statement for Cisco agents which\n            implement the Cisco NTP MIB.')
ciscoNtpMIBComplianceRev3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 1, 4)).setObjects(("CISCO-NTP-MIB", "ciscoNtpSysGroup"), ("CISCO-NTP-MIB", "ciscoNtpPeersGroupRev2"), ("CISCO-NTP-MIB", "ciscoNtpFilterGroup"), ("CISCO-NTP-MIB", "ciscoNtpPeerExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpMIBComplianceRev3 = ciscoNtpMIBComplianceRev3.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoNtpMIBComplianceRev3.setDescription('The compliance statement for Cisco agents which\n            implement the Cisco NTP MIB.')
ciscoNtpMIBComplianceRev4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 1, 5)).setObjects(("CISCO-NTP-MIB", "ciscoNtpSysGroup"), ("CISCO-NTP-MIB", "ciscoNtpPeersGroupRev2"), ("CISCO-NTP-MIB", "ciscoNtpFilterGroup"), ("CISCO-NTP-MIB", "ciscoNtpPeerExtGroup"), ("CISCO-NTP-MIB", "ciscoNtpSysExtGroup"), ("CISCO-NTP-MIB", "ciscoNtpSrvNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpMIBComplianceRev4 = ciscoNtpMIBComplianceRev4.setStatus('current')
if mibBuilder.loadTexts: ciscoNtpMIBComplianceRev4.setDescription('The compliance statement for Cisco agents which\n            implement the Cisco NTP MIB.')
ciscoNtpSysGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2, 1)).setObjects(("CISCO-NTP-MIB", "cntpSysLeap"), ("CISCO-NTP-MIB", "cntpSysStratum"), ("CISCO-NTP-MIB", "cntpSysPrecision"), ("CISCO-NTP-MIB", "cntpSysRootDelay"), ("CISCO-NTP-MIB", "cntpSysRootDispersion"), ("CISCO-NTP-MIB", "cntpSysRefId"), ("CISCO-NTP-MIB", "cntpSysRefTime"), ("CISCO-NTP-MIB", "cntpSysPoll"), ("CISCO-NTP-MIB", "cntpSysPeer"), ("CISCO-NTP-MIB", "cntpSysClock"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpSysGroup = ciscoNtpSysGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoNtpSysGroup.setDescription('The NTP system variables.')
ciscoNtpPeersGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2, 2)).setObjects(("CISCO-NTP-MIB", "cntpPeersConfigured"), ("CISCO-NTP-MIB", "cntpPeersPeerAddress"), ("CISCO-NTP-MIB", "cntpPeersPeerPort"), ("CISCO-NTP-MIB", "cntpPeersHostAddress"), ("CISCO-NTP-MIB", "cntpPeersHostPort"), ("CISCO-NTP-MIB", "cntpPeersLeap"), ("CISCO-NTP-MIB", "cntpPeersMode"), ("CISCO-NTP-MIB", "cntpPeersStratum"), ("CISCO-NTP-MIB", "cntpPeersPeerPoll"), ("CISCO-NTP-MIB", "cntpPeersHostPoll"), ("CISCO-NTP-MIB", "cntpPeersPrecision"), ("CISCO-NTP-MIB", "cntpPeersRootDelay"), ("CISCO-NTP-MIB", "cntpPeersRootDispersion"), ("CISCO-NTP-MIB", "cntpPeersRefId"), ("CISCO-NTP-MIB", "cntpPeersRefTime"), ("CISCO-NTP-MIB", "cntpPeersOrgTime"), ("CISCO-NTP-MIB", "cntpPeersReceiveTime"), ("CISCO-NTP-MIB", "cntpPeersTransmitTime"), ("CISCO-NTP-MIB", "cntpPeersUpdateTime"), ("CISCO-NTP-MIB", "cntpPeersReach"), ("CISCO-NTP-MIB", "cntpPeersTimer"), ("CISCO-NTP-MIB", "cntpPeersOffset"), ("CISCO-NTP-MIB", "cntpPeersDelay"), ("CISCO-NTP-MIB", "cntpPeersDispersion"), ("CISCO-NTP-MIB", "cntpPeersFilterValidEntries"), ("CISCO-NTP-MIB", "cntpPeersEntryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpPeersGroup = ciscoNtpPeersGroup.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoNtpPeersGroup.setDescription('The NTP peer variables.')
ciscoNtpFilterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2, 3)).setObjects(("CISCO-NTP-MIB", "cntpFilterPeersOffset"), ("CISCO-NTP-MIB", "cntpFilterPeersDelay"), ("CISCO-NTP-MIB", "cntpFilterPeersDispersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpFilterGroup = ciscoNtpFilterGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoNtpFilterGroup.setDescription('The NTP clock-filter variables.')
ciscoNtpPeersGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2, 4)).setObjects(("CISCO-NTP-MIB", "cntpPeersConfigured"), ("CISCO-NTP-MIB", "cntpPeersPeerAddress"), ("CISCO-NTP-MIB", "cntpPeersPeerPort"), ("CISCO-NTP-MIB", "cntpPeersHostAddress"), ("CISCO-NTP-MIB", "cntpPeersHostPort"), ("CISCO-NTP-MIB", "cntpPeersLeap"), ("CISCO-NTP-MIB", "cntpPeersMode"), ("CISCO-NTP-MIB", "cntpPeersStratum"), ("CISCO-NTP-MIB", "cntpPeersPeerPoll"), ("CISCO-NTP-MIB", "cntpPeersHostPoll"), ("CISCO-NTP-MIB", "cntpPeersPrecision"), ("CISCO-NTP-MIB", "cntpPeersRootDelay"), ("CISCO-NTP-MIB", "cntpPeersRootDispersion"), ("CISCO-NTP-MIB", "cntpPeersRefId"), ("CISCO-NTP-MIB", "cntpPeersRefTime"), ("CISCO-NTP-MIB", "cntpPeersOrgTime"), ("CISCO-NTP-MIB", "cntpPeersReceiveTime"), ("CISCO-NTP-MIB", "cntpPeersTransmitTime"), ("CISCO-NTP-MIB", "cntpPeersUpdateTimeRev1"), ("CISCO-NTP-MIB", "cntpPeersReach"), ("CISCO-NTP-MIB", "cntpPeersTimer"), ("CISCO-NTP-MIB", "cntpPeersOffset"), ("CISCO-NTP-MIB", "cntpPeersDelay"), ("CISCO-NTP-MIB", "cntpPeersDispersion"), ("CISCO-NTP-MIB", "cntpPeersFilterValidEntries"), ("CISCO-NTP-MIB", "cntpPeersEntryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpPeersGroupRev1 = ciscoNtpPeersGroupRev1.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoNtpPeersGroupRev1.setDescription('The NTP peer variables.')
ciscoNtpPeerExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2, 5)).setObjects(("CISCO-NTP-MIB", "cntpPeersPrefPeer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpPeerExtGroup = ciscoNtpPeerExtGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoNtpPeerExtGroup.setDescription('The extended set of NTP peer variable(s).')
ciscoNtpPeersGroupRev2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2, 6)).setObjects(("CISCO-NTP-MIB", "cntpPeersConfigured"), ("CISCO-NTP-MIB", "cntpPeersPeerAddress"), ("CISCO-NTP-MIB", "cntpPeersPeerPort"), ("CISCO-NTP-MIB", "cntpPeersHostAddress"), ("CISCO-NTP-MIB", "cntpPeersHostPort"), ("CISCO-NTP-MIB", "cntpPeersLeap"), ("CISCO-NTP-MIB", "cntpPeersMode"), ("CISCO-NTP-MIB", "cntpPeersStratum"), ("CISCO-NTP-MIB", "cntpPeersPeerPoll"), ("CISCO-NTP-MIB", "cntpPeersHostPoll"), ("CISCO-NTP-MIB", "cntpPeersPrecision"), ("CISCO-NTP-MIB", "cntpPeersRootDelay"), ("CISCO-NTP-MIB", "cntpPeersRootDispersion"), ("CISCO-NTP-MIB", "cntpPeersRefId"), ("CISCO-NTP-MIB", "cntpPeersRefTime"), ("CISCO-NTP-MIB", "cntpPeersOrgTime"), ("CISCO-NTP-MIB", "cntpPeersReceiveTime"), ("CISCO-NTP-MIB", "cntpPeersTransmitTime"), ("CISCO-NTP-MIB", "cntpPeersUpdateTimeRev1"), ("CISCO-NTP-MIB", "cntpPeersReach"), ("CISCO-NTP-MIB", "cntpPeersTimer"), ("CISCO-NTP-MIB", "cntpPeersOffset"), ("CISCO-NTP-MIB", "cntpPeersDelay"), ("CISCO-NTP-MIB", "cntpPeersDispersion"), ("CISCO-NTP-MIB", "cntpPeersFilterValidEntries"), ("CISCO-NTP-MIB", "cntpPeersEntryStatus"), ("CISCO-NTP-MIB", "cntpPeersPeerName"), ("CISCO-NTP-MIB", "cntpPeersPeerType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpPeersGroupRev2 = ciscoNtpPeersGroupRev2.setStatus('current')
if mibBuilder.loadTexts: ciscoNtpPeersGroupRev2.setDescription('The NTP peer variables.')
ciscoNtpSysExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2, 7)).setObjects(("CISCO-NTP-MIB", "cntpSysSrvStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpSysExtGroup = ciscoNtpSysExtGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoNtpSysExtGroup.setDescription('The extended set of NTP system variable(s).')
ciscoNtpSrvNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2, 8)).setObjects(("CISCO-NTP-MIB", "ciscoNtpSrvStatusChange"), ("CISCO-NTP-MIB", "ciscoNtpHighPriorityConnFailure"), ("CISCO-NTP-MIB", "ciscoNtpHighPriorityConnRestore"), ("CISCO-NTP-MIB", "ciscoNtpGeneralConnFailure"), ("CISCO-NTP-MIB", "ciscoNtpGeneralConnRestore"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpSrvNotifGroup = ciscoNtpSrvNotifGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoNtpSrvNotifGroup.setDescription('The collection of notifications for the NTP Server.')
mibBuilder.exportSymbols("CISCO-NTP-MIB", NTPAssocIdentifier=NTPAssocIdentifier, NTPLeapIndicator=NTPLeapIndicator, NTPPollInterval=NTPPollInterval, NTPRefId=NTPRefId, NTPSignedTimeValue=NTPSignedTimeValue, NTPStratum=NTPStratum, NTPTimeStamp=NTPTimeStamp, NTPUnsignedTimeValue=NTPUnsignedTimeValue, PYSNMP_MODULE_ID=ciscoNtpMIB, ciscoNtpFilterGroup=ciscoNtpFilterGroup, ciscoNtpGeneralConnFailure=ciscoNtpGeneralConnFailure, ciscoNtpGeneralConnRestore=ciscoNtpGeneralConnRestore, ciscoNtpHighPriorityConnFailure=ciscoNtpHighPriorityConnFailure, ciscoNtpHighPriorityConnRestore=ciscoNtpHighPriorityConnRestore, ciscoNtpMIB=ciscoNtpMIB, ciscoNtpMIBCompliance=ciscoNtpMIBCompliance, ciscoNtpMIBComplianceRev1=ciscoNtpMIBComplianceRev1, ciscoNtpMIBComplianceRev2=ciscoNtpMIBComplianceRev2, ciscoNtpMIBComplianceRev3=ciscoNtpMIBComplianceRev3, ciscoNtpMIBComplianceRev4=ciscoNtpMIBComplianceRev4, ciscoNtpMIBCompliances=ciscoNtpMIBCompliances, ciscoNtpMIBConformance=ciscoNtpMIBConformance, ciscoNtpMIBGroups=ciscoNtpMIBGroups, ciscoNtpMIBNotifs=ciscoNtpMIBNotifs, ciscoNtpMIBObjects=ciscoNtpMIBObjects, ciscoNtpPeerExtGroup=ciscoNtpPeerExtGroup, ciscoNtpPeersGroup=ciscoNtpPeersGroup, ciscoNtpPeersGroupRev1=ciscoNtpPeersGroupRev1, ciscoNtpPeersGroupRev2=ciscoNtpPeersGroupRev2, ciscoNtpSrvNotifGroup=ciscoNtpSrvNotifGroup, ciscoNtpSrvStatusChange=ciscoNtpSrvStatusChange, ciscoNtpSysExtGroup=ciscoNtpSysExtGroup, ciscoNtpSysGroup=ciscoNtpSysGroup, cntpFilter=cntpFilter, cntpFilterIndex=cntpFilterIndex, cntpFilterPeersDelay=cntpFilterPeersDelay, cntpFilterPeersDispersion=cntpFilterPeersDispersion, cntpFilterPeersOffset=cntpFilterPeersOffset, cntpFilterRegisterEntry=cntpFilterRegisterEntry, cntpFilterRegisterTable=cntpFilterRegisterTable, cntpPeers=cntpPeers, cntpPeersAssocId=cntpPeersAssocId, cntpPeersConfigured=cntpPeersConfigured, cntpPeersDelay=cntpPeersDelay, cntpPeersDispersion=cntpPeersDispersion, cntpPeersEntryStatus=cntpPeersEntryStatus, cntpPeersFilterValidEntries=cntpPeersFilterValidEntries, cntpPeersHostAddress=cntpPeersHostAddress, cntpPeersHostPoll=cntpPeersHostPoll, cntpPeersHostPort=cntpPeersHostPort, cntpPeersLeap=cntpPeersLeap, cntpPeersMode=cntpPeersMode, cntpPeersOffset=cntpPeersOffset, cntpPeersOrgTime=cntpPeersOrgTime, cntpPeersPeerAddress=cntpPeersPeerAddress, cntpPeersPeerName=cntpPeersPeerName, cntpPeersPeerPoll=cntpPeersPeerPoll, cntpPeersPeerPort=cntpPeersPeerPort, cntpPeersPeerType=cntpPeersPeerType, cntpPeersPrecision=cntpPeersPrecision, cntpPeersPrefPeer=cntpPeersPrefPeer, cntpPeersReach=cntpPeersReach, cntpPeersReceiveTime=cntpPeersReceiveTime, cntpPeersRefId=cntpPeersRefId, cntpPeersRefTime=cntpPeersRefTime, cntpPeersRootDelay=cntpPeersRootDelay, cntpPeersRootDispersion=cntpPeersRootDispersion, cntpPeersStratum=cntpPeersStratum, cntpPeersTimer=cntpPeersTimer, cntpPeersTransmitTime=cntpPeersTransmitTime, cntpPeersUpdateTime=cntpPeersUpdateTime, cntpPeersUpdateTimeRev1=cntpPeersUpdateTimeRev1, cntpPeersVarEntry=cntpPeersVarEntry, cntpPeersVarTable=cntpPeersVarTable, cntpSysClock=cntpSysClock, cntpSysLeap=cntpSysLeap, cntpSysPeer=cntpSysPeer, cntpSysPoll=cntpSysPoll, cntpSysPrecision=cntpSysPrecision, cntpSysRefId=cntpSysRefId, cntpSysRefTime=cntpSysRefTime, cntpSysRootDelay=cntpSysRootDelay, cntpSysRootDispersion=cntpSysRootDispersion, cntpSysSrvStatus=cntpSysSrvStatus, cntpSysStratum=cntpSysStratum, cntpSystem=cntpSystem)
