#
# PySNMP MIB module PAN-GLOBAL-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/paloaltonetworks/PAN-GLOBAL-TC-MIB
# Produced by pysmi-1.1.10 at Fri Nov 10 13:26:57 2023
# On host fv-az1435-737 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
panModules, = mibBuilder.importSymbols("PAN-GLOBAL-REG", "panModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Bits, TimeTicks, iso, MibIdentifier, ModuleIdentity, Unsigned32, IpAddress, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "TimeTicks", "iso", "MibIdentifier", "ModuleIdentity", "Unsigned32", "IpAddress", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
panGlobalTcModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 25461, 1, 1, 2))
panGlobalTcModule.setRevisions(('2011-02-09 16:10',))
if mibBuilder.loadTexts: panGlobalTcModule.setLastUpdated('201106271040Z')
if mibBuilder.loadTexts: panGlobalTcModule.setOrganization('Palo Alto Networks')
class TcAppaname(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class TcChassisType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

mibBuilder.exportSymbols("PAN-GLOBAL-TC", TcAppaname=TcAppaname, PYSNMP_MODULE_ID=panGlobalTcModule, panGlobalTcModule=panGlobalTcModule, TcChassisType=TcChassisType)
