#
# PySNMP MIB module CISCO-ENTITY-DIAG-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ENTITY-DIAG-TC-MIB
# Source digest sha256:bf1ff7cdf4bb186607d3c06f3660789345d3bd0ac04f320e0e030eca0187ed84
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEntityDiagTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 584))
ciscoEntityDiagTcMIB.setRevisions(('2009-07-01 00:00', '2006-12-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEntityDiagTcMIB.setRevisionsDescriptions(("Added enumeration 'none' to CeDiagTestIdentifier.", 'The initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoEntityDiagTcMIB.setLastUpdated('2009-07-01 00:00')
if mibBuilder.loadTexts: ciscoEntityDiagTcMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEntityDiagTcMIB.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA 95134\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-online-diag@cisco.com')
if mibBuilder.loadTexts: ciscoEntityDiagTcMIB.setDescription('This module defines the textual conventions used within\n        Cisco Entity Diag MIB.')
class CeDiagDiagnosticLevel(TextualConvention, Integer32):
    description = "The relative degree of completeness that a test will exercise\n        a physical entity:\n\n        'bypass'   - indicates that no testing should be performed.\n\n        'minimal'  - indicates that the physical entity will only\n                     execute those tests characterized as minimal tests.\n\n        'complete' - indicates that the physical entity will execute\n                     those tests characterized as minimal or complete\n                     tests."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("bypass", 1), ("minimal", 2), ("complete", 3))

class CeDiagDiagnosticMethod(TextualConvention, Integer32):
    description = "The method used to invoke a diagnostic:\n\n        'bootup'        - specifies a diagnostic invoked by a physical\n                          entity during its boot-up process.\n\n        'onDemand'      - specifies a diagnostic invoked by a management\n                          application or through some other management\n                          interface, such as a command console.\n\n        'scheduled'     - specifies a diagnostic invoked by the job\n                          scheduler.\n\n        'healthMonitor' - specifies a diagnostic invoked by a health\n                          monitor.\n\n        'none'          - no diagnostic method is invoked."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("bootup", 1), ("onDemand", 2), ("scheduled", 3), ("healthMonitor", 4), ("none", 5))

class CeDiagTestIdentifier(TextualConvention, Unsigned32):
    description = 'An arbitrary positive integer value that uniquely identifies a\n        test.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CeDiagErrorIdentifier(TextualConvention, Unsigned32):
    description = 'An arbitrary integer value that uniquely identifies an error\n        code.  An error code maps to a message specifying details or\n        a reason why test failed.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CeDiagErrorIdentifierOrZero(TextualConvention, Unsigned32):
    description = "An arbitrary integer value that uniquely identifies an error\n        code.  An error code maps to a message specifying details or\n        a reason why a test failed.  An object having a value of '0'\n        specifies 'no error message'."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class CeDiagJobIdentifier(TextualConvention, Unsigned32):
    description = 'An arbitrary non-zero integer value that uniquely identifies a\n        single job with respect to a physical entity.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CeDiagPortList(TextualConvention, OctetString):
    description = "The entPhysicalTable contains conceptual rows representing\n        ports, each having a value that uniquely identifies the port\n        relative to its parent physical entity (example: the value of\n        entPhysicalParentRelPos or external labeling of port).  This \n        MIB definition assumes that these values are relatively\n        small integers.\n\n        An OCTET STRING representing a list of ports, in which each bit\n        represents a single port.  The bits in the first octet\n        represent ports identified by the integer values 1 through 8,\n        inclusive, The bits in the second octet represent ports\n        identified by the integer values 9 through 16, inclusive, and\n        so forth.\n\n        Within each octet, the most significant bit of an octet\n        represents the port identified by the lowest integer value, and\n        the least significant bit represents the port identified by the\n        highest integer value.\n\n        The figure shown below illustrates the format of a port list 8\n        octets in length.\n\n         Octet 1             Octet 32\n\n         7 6 5 4 3 2 1 0     7 6 5 4 3 2 1 0\n        +-+-+-+-+-+-+-+-+   +-+-+-+-+-+-+-+-+\n        |               |...|               |\n        +-+-+-+-+-+-+-+-+   +-+-+-+-+-+-+-+-+\n         | | | | | | | |     | | | | | | | |\n         | | | | | | | |     | | | | | | | +- Port 255\n         | | | | | | | |     | | | | | | +--- Port 254\n         | | | | | | | |     | | | | | +----- Port 253\n         | | | | | | | |     | | | | +------- Port 252\n         | | | | | | | |     | | | +--------- Port 251\n         | | | | | | | |     | | +----------- Port 250\n         | | | | | | | |     | +------------- Port 249\n         | | | | | | | |     +--------------- Port 248\n         | | | | | | | |                          :\n         | | | | | | | |                          :\n         | | | | | | | +--------------------- Port 7\n         | | | | | | +----------------------- Port 6\n         | | | | | +------------------------- Port 5\n         | | | | +--------------------------- Port 4\n         | | | +----------------------------- Port 3\n         | | +------------------------------- Port 2\n         | +--------------------------------- Port 1\n         +----------------------------------- Port 0\n\n        An port list of length N, where N < 32, represents a port list\n        for which ports assigned identifiers greater than or equal to\n        N*8 have the value of '0'.\n\n        A special case is a port list having a length of '0', which\n        represents the empty set (i.e., no ports).\n\n        Observe that care should be taken to concerning the numbering\n        of ports relative to their parent physical entity.  Some\n        implementations base their numbering at '0' and others base\n        their numbering at '1'.  To avert any problems introduced by\n        such inconsistencies, the management application should pay\n        attention to the contents of the entPhysicalTable when\n        constructing a port list."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class CeDiagTestList(TextualConvention, OctetString):
    description = "For each unique type of physical entity (i.e., for each set of\n        physical entities sharing a unique entPhysicalVendorType OID),\n        there an exists unique test space.  Observe that it is not\n        necessary that all the tests within a space be defined.\n\n        An OCTET STRING represents an test list, in which each bit\n        represents a single test.  The bits in the first octet\n        represent tests identified by the integer values 1 through 8,\n        inclusive, The bits in the second octet represent tests\n        identified by the integer values 9 through 16, inclusive, and\n        so forth.\n\n        Within each octet, the most significant bit of an octet\n        represents the test identified by the lowest integer value, and\n        the least significant bit represents the test identified by the\n        highest integer value.\n\n        The figure shown below illustrates the format of an test list.\n\n         Octet 1             Octet 32\n\n         7 6 5 4 3 2 1 0     7 6 5 4 3 2 1 0\n        +-+-+-+-+-+-+-+-+   +-+-+-+-+-+-+-+-+\n        |               |...|               |\n        +-+-+-+-+-+-+-+-+   +-+-+-+-+-+-+-+-+\n         | | | | | | | |     | | | | | | | |\n         | | | | | | | |     | | | | | | | +- Test 255\n         | | | | | | | |     | | | | | | +--- Test 254\n         | | | | | | | |     | | | | | +----- Test 253\n         | | | | | | | |     | | | | +------- Test 252\n         | | | | | | | |     | | | +--------- Test 251\n         | | | | | | | |     | | +----------- Test 250\n         | | | | | | | |     | +------------- Test 249\n         | | | | | | | |     +--------------- Test 248\n         | | | | | | | |                          :\n         | | | | | | | |                          :\n         | | | | | | | +--------------------- Test 7\n         | | | | | | +----------------------- Test 6\n         | | | | | +------------------------- Test 5\n         | | | | +--------------------------- Test 4\n         | | | +----------------------------- Test 3\n         | | +------------------------------- Test 2\n         | +--------------------------------- Test 1\n         +----------------------------------- Test 0\n\n        An test list of length N, where N < 32, represents a test list\n        for which test N*8 through 255 have the value of '0'.  A special\n        case is a test list having a length of '0', which represents a\n        test list of all zeros."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class CeDiagJobSuite(TextualConvention, Integer32):
    description = "This object indicates the various system predefined test\n        suites a diagnostic job can choose from.\n\n        'none'             - indicates that there is no job suite\n                             specified.\n\n        'complete'         - indicates that this job will run the\n                             complete tests on the physical \n                             entity.\n\n        'minimal'          - indicates that this job will run the\n                             minimal tests on the physical \n                             entity.\n\n        'nonDisruptive'    - indicates that this job will run the\n                             nonDisruptive tests on the physical \n                             entity.\n\n        'perPort'          - indicates that this job will run the\n                             perPort tests on the physical \n                             entity."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 1), ("complete", 2), ("minimal", 3), ("nonDisruptive", 4), ("perPort", 5))

mibBuilder.exportSymbols("CISCO-ENTITY-DIAG-TC-MIB", CeDiagDiagnosticLevel=CeDiagDiagnosticLevel, CeDiagDiagnosticMethod=CeDiagDiagnosticMethod, CeDiagErrorIdentifier=CeDiagErrorIdentifier, CeDiagErrorIdentifierOrZero=CeDiagErrorIdentifierOrZero, CeDiagJobIdentifier=CeDiagJobIdentifier, CeDiagJobSuite=CeDiagJobSuite, CeDiagPortList=CeDiagPortList, CeDiagTestIdentifier=CeDiagTestIdentifier, CeDiagTestList=CeDiagTestList, PYSNMP_MODULE_ID=ciscoEntityDiagTcMIB, ciscoEntityDiagTcMIB=ciscoEntityDiagTcMIB)
