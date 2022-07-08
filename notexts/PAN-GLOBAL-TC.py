#
# PySNMP MIB module PAN-GLOBAL-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/paloaltonetworks/PAN-GLOBAL-TC-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:00:14 2022
# On host fv-az42-349 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
panModules, = mibBuilder.importSymbols("PAN-GLOBAL-REG", "panModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, NotificationType, ObjectIdentity, ModuleIdentity, Counter64, Integer32, iso, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "ObjectIdentity", "ModuleIdentity", "Counter64", "Integer32", "iso", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "TimeTicks", "Gauge32")
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

mibBuilder.exportSymbols("PAN-GLOBAL-TC", TcAppaname=TcAppaname, PYSNMP_MODULE_ID=panGlobalTcModule, TcChassisType=TcChassisType, panGlobalTcModule=panGlobalTcModule)
