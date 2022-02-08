#
# PySNMP MIB module PAN-GLOBAL-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/paloaltonetworks/PAN-GLOBAL-TC-MIB
# Produced by pysmi-1.1.8 at Tue Feb  8 22:12:54 2022
# On host fv-az126-754 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
panModules, = mibBuilder.importSymbols("PAN-GLOBAL-REG", "panModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Counter32, Unsigned32, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, TimeTicks, ObjectIdentity, ModuleIdentity, Counter64, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "Unsigned32", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "Counter64", "NotificationType", "iso")
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
