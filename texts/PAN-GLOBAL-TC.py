#
# PySNMP MIB module PAN-GLOBAL-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/paloaltonetworks/PAN-GLOBAL-TC-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 13:44:27 2023
# On host fv-az210-608 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
panModules, = mibBuilder.importSymbols("PAN-GLOBAL-REG", "panModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Unsigned32, TimeTicks, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Counter32, IpAddress, MibIdentifier, ObjectIdentity, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "TimeTicks", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Counter32", "IpAddress", "MibIdentifier", "ObjectIdentity", "Integer32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
panGlobalTcModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 25461, 1, 1, 2))
panGlobalTcModule.setRevisions(('2011-02-09 16:10',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: panGlobalTcModule.setRevisionsDescriptions(('\n\t\t\tRev 1.0\n\t\t\tInitial version of MIB module PAN-GLOBAL-TC.',))
if mibBuilder.loadTexts: panGlobalTcModule.setLastUpdated('201106271040Z')
if mibBuilder.loadTexts: panGlobalTcModule.setOrganization('Palo Alto Networks')
if mibBuilder.loadTexts: panGlobalTcModule.setContactInfo('\n\t\t\t\t\tCustomer Support\n\t\t\t\t\tPalo Alto Networks\n\t\t\t\t\t4401 Great America Pkwy\n\t\t\t\t\tSanta Clara, CA 95054-1211\n\n\t\t\t\t\t+1 866-898-9087\n\t\t\t\t\tsupport at paloaltonetworks dot com')
if mibBuilder.loadTexts: panGlobalTcModule.setDescription("\n\t\t\tA MIB module containing textual conventions\n\t\t\tfor Palo Alto Networks' enterprise MIB modules.\n\t\t\tThese textual conventions are used across all Palo Alto products.")
class TcAppaname(TextualConvention, OctetString):
    description = "\n\t\t\tRepresents the name of an application.\n\n\t\t\tThis has all the restrictions of the DisplayString textual\n\t\t\tconvention with the following additional ones:\n\n\t\t\t- Only the following characters/character ranges are allowed:\n\t\t\t\t0-9\n\t\t\t\tA-Z\n\t\t\t\ta-z\n\t\t\t\t:./#$&_-+()'\n\t\t\t\t<space>\n\n\t\t\tAny object defined using this syntax may not exceed 64\n\t\t\tcharacters in length."
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class TcChassisType(TextualConvention, OctetString):
    description = '\n\t\t\tEnumerates all possible chassis types for Palo Alto devices.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

mibBuilder.exportSymbols("PAN-GLOBAL-TC", panGlobalTcModule=panGlobalTcModule, TcChassisType=TcChassisType, TcAppaname=TcAppaname, PYSNMP_MODULE_ID=panGlobalTcModule)
